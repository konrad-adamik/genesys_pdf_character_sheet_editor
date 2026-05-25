from __future__ import annotations

import io
import json
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import BooleanObject, NameObject, NumberObject
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

from utils.skills import CHARACTERISTIC_KEYS, SKILL_ROWS, SKILL_ROWS_BY_SLUG, SKILL_SLUGS


FIELD_ALIASES = {
    "woundThreshold": "wound_threshold",
    "strainThreshold": "strain_threshold",
    "meleeDefense": "melee_defense",
    "rangedDefense": "ranged_defense",
    "skillRanks": "skill_ranks",
    "skillLabels": "skill_labels",
    "skillCharacteristics": "skill_characteristics",
    "skillUniverse": "skill_universe",
    "skillProfession": "skill_profession",
    "talentRows": "talent_rows",
    "weaponRows": "weapon_rows",
}

PDF_FIELD_MAP = {
    "name": "IMI\u0118 POSTACI",
    "player": "GRACZ",
    "career": "PROFESJA",
    "archetype": "GATUNEK/ARCHETYP",
    "brawn": "krzepa",
    "agility": "zwinno\u015b\u0107",
    "intellect": "intelekt",
    "cunning": "spryt",
    "willpower": "wola",
    "presence": "prezencja",
    "soak": "redukcja",
    "wound_threshold": "pr\u00f3g 1",
    "strain_threshold": "pr\u00f3g 2",
    "advantage": "zaleta",
    "flaw": "wada",
    "desire": "pragnienie",
    "fear": "lęk",
    "armor_weapons": "broń i pancerz",
    "notes": "NOTATKI",
    "equipment": "sprz\u0119t osobisty",
    "money": "pieniądze",
    "sex": "PŁEĆ",
    "age": "WIEK",
    "height": "WZROST",
    "body_build": "BUDOWA CIAŁA",
    "hair": "WŁOSY",
    "eyes": "OCZY",
    "distinctive_marks": "ZNAKI SZCZEGÓLNE",
}

WEAPON_NAME_FIELDS = ["fill_1", "fill_2", "fill_3", "fill_4"]
WEAPON_SKILL_FIELDS = ["fill_5", "fill_6", "fill_7", "fill_8"]
WEAPON_DAMAGE_FIELDS = ["fill_9", "fill_10", "fill_11", "fill_12"]
WEAPON_CRIT_FIELDS = ["fill_13", "fill_14", "fill_15", "fill_16"]
WEAPON_RANGE_FIELDS = ["fill_17", "fill_18", "fill_19", "fill_20"]
WEAPON_SPECIAL_FIELDS = ["SPECJALNE 1", "SPECJALNE 2", "SPECJALNE 3", "SPECJALNE 4"]
TALENT_NAME_FIELDS = [f"nazwa {index}" for index in range(1, 13)]
TALENT_PAGE_FIELDS = [f"s {index}" for index in range(1, 13)]
TALENT_DESC_FIELDS = [f"opis {index}" for index in range(1, 13)]

SKILL_GREEN = HexColor("#6E8F20")
SKILL_YELLOW = HexColor("#FCB104")
SKILL_DISABLED = HexColor("#D7DBDE")


def normalize_character_data(data: dict) -> dict:
    normalized = dict(data)
    for source_key, target_key in FIELD_ALIASES.items():
        if source_key in normalized and target_key not in normalized:
            normalized[target_key] = normalized[source_key]
    return normalized


def stringify(value) -> str:
    if value is None:
        return ""
    return str(value)


def clamp_int(value, minimum: int = 0, maximum: int = 99, fallback: int = 0) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return fallback
    return max(minimum, min(maximum, parsed))


def split_lines(value: str) -> list[str]:
    return [line.strip() for line in stringify(value).splitlines() if line.strip()]


def parse_weapon_rows(value: str) -> list[dict[str, str]]:
    rows = []
    for line in split_lines(value):
        parts = [part.strip() for part in line.split("|")]
        rows.append(
            {
                "name": parts[0] if len(parts) > 0 else "",
                "skill": parts[1] if len(parts) > 1 else "",
                "damage": parts[2] if len(parts) > 2 else "",
                "crit": parts[3] if len(parts) > 3 else "",
                "range": parts[4] if len(parts) > 4 else "",
                "special": parts[5] if len(parts) > 5 else "",
            }
        )
    return rows


def extract_weapon_rows(normalized: dict) -> list[dict[str, str]]:
    raw_rows = normalized.get("weapon_rows", normalized.get("weaponRows"))
    if isinstance(raw_rows, list):
        rows: list[dict[str, str]] = []
        for row in raw_rows[:4]:
            if not isinstance(row, dict):
                continue
            rows.append(
                {
                    "name": stringify(row.get("name", "")).strip(),
                    "skill": stringify(row.get("skill", "")).strip(),
                    "damage": stringify(row.get("damage", "")).strip(),
                    "crit": stringify(row.get("crit", "")).strip(),
                    "range": stringify(row.get("range", "")).strip(),
                    "special": stringify(row.get("special", "")).strip(),
                }
            )
        return rows

    if isinstance(normalized.get("weapons"), str):
        return parse_weapon_rows(normalized.get("weapons", ""))

    if isinstance(raw_rows, str):
        return parse_weapon_rows(raw_rows)

    return []


def extract_talent_rows(normalized: dict) -> list[dict[str, str]]:
    raw_rows = normalized.get("talent_rows", normalized.get("talentRows"))
    if isinstance(raw_rows, list):
        rows: list[dict[str, str]] = []
        for row in raw_rows[:12]:
            if not isinstance(row, dict):
                continue
            rows.append(
                {
                    "name": stringify(row.get("name", "")).strip(),
                    "page": stringify(row.get("page", "")).strip(),
                    "description": stringify(row.get("description", "")).strip(),
                }
            )
        return rows

    if isinstance(normalized.get("talents"), str):
        rows = []
        for line in split_lines(normalized.get("talents", ""))[:12]:
            parts = [part.strip() for part in line.split("|")]
            rows.append(
                {
                    "name": parts[0] if len(parts) > 0 else "",
                    "page": parts[1] if len(parts) > 1 else "",
                    "description": parts[2] if len(parts) > 2 else "",
                }
            )
        return rows

    return []


def assign_repeated_fields(field_values: dict[str, str], source_lines: list[str], pdf_fields: list[str]) -> None:
    for index, pdf_field in enumerate(pdf_fields):
        field_values[pdf_field] = source_lines[index] if index < len(source_lines) else ""


def extract_skill_ranks(normalized: dict) -> dict[str, int]:
    raw_ranks = normalized.get("skill_ranks", {})
    if not isinstance(raw_ranks, dict):
        return {slug: 0 for slug in SKILL_SLUGS}

    skill_ranks: dict[str, int] = {}
    for slug in SKILL_SLUGS:
        skill_ranks[slug] = clamp_int(raw_ranks.get(slug, 0), minimum=0, maximum=5, fallback=0)
    return skill_ranks


def extract_skill_labels(normalized: dict) -> dict[str, str]:
    raw_labels = normalized.get("skill_labels", {})
    if not isinstance(raw_labels, dict):
        return {}
    return {slug: stringify(raw_labels.get(slug, "")).strip() for slug in SKILL_SLUGS}


def extract_skill_characteristics(normalized: dict) -> dict[str, str]:
    raw_characteristics = normalized.get("skill_characteristics", {})
    if not isinstance(raw_characteristics, dict):
        raw_characteristics = {}

    result: dict[str, str] = {}
    for slug in SKILL_SLUGS:
        row = SKILL_ROWS_BY_SLUG[slug]
        default_abbr = stringify(row["abbr"]).strip()
        if row.get("editable_characteristic"):
            selected = stringify(raw_characteristics.get(slug, "")).strip().upper()
            result[slug] = selected if selected in CHARACTERISTIC_KEYS else ""
        else:
            selected = stringify(raw_characteristics.get(slug, default_abbr)).strip().upper() or default_abbr
            result[slug] = selected if selected in CHARACTERISTIC_KEYS else default_abbr
    return result


def extract_skill_boolean_map(normalized: dict, key: str, default: bool) -> dict[str, bool]:
    raw_values = normalized.get(key, {})
    if not isinstance(raw_values, dict):
        raw_values = {}

    result: dict[str, bool] = {}
    for slug in SKILL_SLUGS:
        value = raw_values.get(slug, default)
        if isinstance(value, str):
            result[slug] = value.strip().lower() in {"1", "true", "tak", "yes", "on"}
        else:
            result[slug] = bool(value)
    return result


def map_character_to_pdf_fields(data: dict) -> dict[str, str]:
    normalized = normalize_character_data(data)
    field_values: dict[str, str] = {}
    skill_labels = extract_skill_labels(normalized)

    for key, pdf_field in PDF_FIELD_MAP.items():
        value = normalized.get(key)
        if value is None:
            continue
        field_values[pdf_field] = stringify(value)

    talent_rows = extract_talent_rows(normalized)
    assign_repeated_fields(field_values, [row["name"] for row in talent_rows], TALENT_NAME_FIELDS)
    assign_repeated_fields(field_values, [row["page"] for row in talent_rows], TALENT_PAGE_FIELDS)
    assign_repeated_fields(field_values, [row["description"] for row in talent_rows], TALENT_DESC_FIELDS)
    weapon_rows = extract_weapon_rows(normalized)
    assign_repeated_fields(field_values, [row["name"] for row in weapon_rows], WEAPON_NAME_FIELDS)
    assign_repeated_fields(field_values, [row["skill"] for row in weapon_rows], WEAPON_SKILL_FIELDS)
    assign_repeated_fields(field_values, [row["damage"] for row in weapon_rows], WEAPON_DAMAGE_FIELDS)
    assign_repeated_fields(field_values, [row["crit"] for row in weapon_rows], WEAPON_CRIT_FIELDS)
    assign_repeated_fields(field_values, [row["range"] for row in weapon_rows], WEAPON_RANGE_FIELDS)
    assign_repeated_fields(field_values, [row["special"] for row in weapon_rows], WEAPON_SPECIAL_FIELDS)

    if "current_wounds" in normalized:
        field_values["aktualne 1"] = stringify(normalized["current_wounds"])
    if "current_strain" in normalized:
        field_values["aktualne 2"] = stringify(normalized["current_strain"])

    field_values["pr\u00f3g 3"] = stringify(normalized.get("ranged_defense", 0))
    field_values["aktualne 3"] = stringify(normalized.get("melee_defense", 0))

    for row in SKILL_ROWS:
        label_field = row.get("label_field")
        if not label_field:
            continue
        slug = row["slug"]
        if row.get("editable_label"):
            field_values[label_field] = skill_labels.get(slug, "")
        else:
            field_values[label_field] = skill_labels.get(slug) or stringify(row["label"])

    return field_values


def build_skill_rect_map(page) -> dict[str, tuple[float, float, float, float]]:
    rects: dict[str, tuple[float, float, float, float]] = {}
    for annot_ref in page.get("/Annots") or []:
        annot = annot_ref.get_object()
        name = annot.get("/T")
        rect = annot.get("/Rect")
        if not name or not rect:
            continue
        rects[str(name)] = tuple(float(value) for value in rect)
    return rects


def skill_box_colors(characteristic_value: int, rank_value: int) -> list[HexColor | None]:
    if rank_value <= characteristic_value:
        yellow_count = min(5, rank_value)
        green_count = min(5 - yellow_count, max(0, characteristic_value - rank_value))
    else:
        yellow_count = min(5, rank_value)
        green_count = 0 if yellow_count >= 5 else 1

    colors: list[HexColor | None] = []
    colors.extend([SKILL_YELLOW] * yellow_count)
    colors.extend([SKILL_GREEN] * green_count)
    while len(colors) < 5:
        colors.append(None)
    return colors


def build_skill_overlay(reader: PdfReader, data: dict) -> bytes | None:
    normalized = normalize_character_data(data)
    skill_ranks = extract_skill_ranks(normalized)
    skill_labels = extract_skill_labels(normalized)
    skill_characteristics = extract_skill_characteristics(normalized)
    skill_universe = extract_skill_boolean_map(normalized, "skill_universe", True)
    page = reader.pages[0]
    rect_map = build_skill_rect_map(page)
    width = float(page.mediabox.width)
    height = float(page.mediabox.height)

    overlay_stream = io.BytesIO()
    overlay_canvas = canvas.Canvas(overlay_stream, pagesize=(width, height))
    drew_anything = False

    for row in SKILL_ROWS:
        slug = row["slug"]
        is_custom_blank = row.get("editable_label") and not skill_labels.get(slug, "").strip()
        if is_custom_blank:
            continue
        characteristic_abbr = skill_characteristics.get(slug, stringify(row["abbr"]))
        characteristic_key = CHARACTERISTIC_KEYS.get(characteristic_abbr)
        pdf_fields = row["pdf_fields"]
        characteristic_value = clamp_int(normalized.get(characteristic_key, 0), minimum=0, maximum=5, fallback=0) if characteristic_key else 0
        rank_value = skill_ranks.get(slug, 0)
        is_universal = skill_universe.get(slug, True)

        row_rects = [rect_map.get(field_name) for field_name in pdf_fields if rect_map.get(field_name) is not None]
        universe_rect = rect_map.get(row.get("universe_field", ""))
        profession_rect = rect_map.get(row.get("profession_field", ""))
        if not is_universal and row_rects and universe_rect and profession_rect:
            all_rects = row_rects + [universe_rect, profession_rect]
            x1 = min(float(rect[0]) for rect in all_rects) - 4
            y1 = min(float(rect[1]) for rect in all_rects) - 1
            x2 = max(float(rect[2]) for rect in all_rects) + 2
            y2 = max(float(rect[3]) for rect in all_rects) + 1
            if hasattr(overlay_canvas, "setFillAlpha"):
                overlay_canvas.setFillAlpha(0.65)
            overlay_canvas.setFillColor(SKILL_DISABLED)
            overlay_canvas.rect(x1, y1, x2 - x1, y2 - y1, fill=1, stroke=0)
            if hasattr(overlay_canvas, "setFillAlpha"):
                overlay_canvas.setFillAlpha(1)
            drew_anything = True

        for field_name, fill_color in zip(pdf_fields, skill_box_colors(characteristic_value, rank_value) if is_universal else [None] * 5):
            if fill_color is None:
                continue
            rect = rect_map.get(field_name)
            if rect is None:
                continue

            x1, y1, x2, y2 = rect
            inset = 1.15
            overlay_canvas.setFillColor(fill_color)
            overlay_canvas.setStrokeColor(fill_color)
            overlay_canvas.rect(
                x1 + inset,
                y1 + inset,
                max(0.0, (x2 - x1) - (inset * 2)),
                max(0.0, (y2 - y1) - (inset * 2)),
                fill=1,
                stroke=0,
            )
            drew_anything = True

    overlay_canvas.save()
    if not drew_anything:
        return None
    return overlay_stream.getvalue()


def hide_skill_widgets(writer: PdfWriter) -> None:
    page = writer.pages[0]
    skill_field_names = {field_name for row in SKILL_ROWS for field_name in row["pdf_fields"]}
    for annot_ref in page.get("/Annots") or []:
        annot = annot_ref.get_object()
        name = annot.get("/T")
        if not name or str(name) not in skill_field_names:
            continue
        annot[NameObject("/F")] = NumberObject(2)
        annot[NameObject("/AS")] = NameObject("/Off")
        annot[NameObject("/V")] = NameObject("/Off")


def apply_skill_checkboxes(writer: PdfWriter, data: dict) -> None:
    normalized = normalize_character_data(data)
    skill_universe = extract_skill_boolean_map(normalized, "skill_universe", True)
    skill_profession = extract_skill_boolean_map(normalized, "skill_profession", False)
    skill_labels = extract_skill_labels(normalized)
    page = writer.pages[0]
    widget_map = {}
    for annot_ref in page.get("/Annots") or []:
        annot = annot_ref.get_object()
        name = annot.get("/T")
        if name:
            widget_map[str(name)] = annot

    for row in SKILL_ROWS:
        slug = row["slug"]
        is_custom_blank = row.get("editable_label") and not skill_labels.get(slug, "").strip()
        checkbox_states = [
            (row.get("universe_field"), skill_universe.get(slug, True) and not is_custom_blank),
            (row.get("profession_field"), skill_profession.get(slug, False) and not is_custom_blank),
        ]
        for field_name, checked in checkbox_states:
            if not field_name:
                continue
            annot = widget_map.get(str(field_name))
            if annot is None:
                continue
            annot[NameObject("/AS")] = NameObject("/Tak" if checked else "/Off")
            annot[NameObject("/V")] = NameObject("/Tak" if checked else "/Off")


def apply_need_appearances(writer: PdfWriter) -> None:
    if "/AcroForm" not in writer._root_object:
        return
    writer._root_object["/AcroForm"][NameObject("/NeedAppearances")] = BooleanObject(True)


def build_filled_pdf_bytes(data: dict, template_path: Path, debug_grid: bool = False) -> bytes:
    del debug_grid
    reader = PdfReader(str(template_path))
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)

    field_values = map_character_to_pdf_fields(data)
    for page in writer.pages:
        writer.update_page_form_field_values(page, field_values, auto_regenerate=True)

    overlay_bytes = build_skill_overlay(reader, data)
    hide_skill_widgets(writer)
    apply_skill_checkboxes(writer, data)
    if overlay_bytes:
        overlay_reader = PdfReader(io.BytesIO(overlay_bytes))
        writer.pages[0].merge_page(overlay_reader.pages[0])

    apply_need_appearances(writer)

    output = io.BytesIO()
    writer.write(output)
    return output.getvalue()


def load_character(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as stream:
        return normalize_character_data(json.load(stream))
