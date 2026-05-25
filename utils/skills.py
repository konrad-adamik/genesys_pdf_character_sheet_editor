from __future__ import annotations

from typing import Final


CHARACTERISTIC_KEYS: Final[dict[str, str]] = {
    "K": "brawn",
    "Z": "agility",
    "I": "intellect",
    "S": "cunning",
    "W": "willpower",
    "P": "presence",
}

CHARACTERISTIC_LABELS: Final[dict[str, str]] = {
    "K": "Krzepa",
    "Z": "Zwinność",
    "I": "Intelekt",
    "S": "Spryt",
    "W": "Wola",
    "P": "Prezencja",
}


def field_group(prefix: str, start: int) -> list[str]:
    return [f"{prefix}{offset}" for offset in range(start, start + 5)]


def skill_row(
    slug: str,
    label: str,
    abbr: str,
    characteristic: str,
    pdf_fields: list[str],
    *,
    universe_field: str | None = None,
    profession_field: str | None = None,
    label_field: str | None = None,
    editable_label: bool = False,
    editable_characteristic: bool = False,
) -> dict[str, object]:
    return {
        "slug": slug,
        "label": label,
        "abbr": abbr,
        "characteristic": characteristic,
        "pdf_fields": pdf_fields,
        "universe_field": universe_field,
        "profession_field": profession_field,
        "label_field": label_field,
        "editable_label": editable_label,
        "editable_characteristic": editable_characteristic,
    }


SKILL_ROWS: Final[list[dict[str, object]]] = [
    skill_row("alchemia", "Alchemia", "I", "intellect", field_group("C", 1), universe_field="ON 1", profession_field="ON 21"),
    skill_row("astrokartografia", "Astrokartografia", "I", "intellect", field_group("C", 6), universe_field="ON 2", profession_field="ON 22"),
    skill_row("atletyka", "Atletyka", "K", "brawn", field_group("C", 11), universe_field="ON 3", profession_field="ON 23"),
    skill_row("czujnosc", "Czujność", "W", "willpower", field_group("C", 16), universe_field="ON 4", profession_field="ON 24"),
    skill_row("dyscyplina", "Dyscyplina", "W", "willpower", field_group("C", 21), universe_field="ON 5", profession_field="ON 25"),
    skill_row("jezdziectwo", "Jeździectwo", "Z", "agility", field_group("C", 26), universe_field="ON 6", profession_field="ON 26"),
    skill_row("komputery", "Komputery", "I", "intellect", field_group("C", 31), universe_field="ON 7", profession_field="ON 27"),
    skill_row("koordynacja", "Koordynacja", "Z", "agility", field_group("C", 36), universe_field="ON 8", profession_field="ON 28"),
    skill_row("machlojki", "Machlojki", "S", "cunning", field_group("C", 41), universe_field="ON 9", profession_field="ON 29"),
    skill_row("mechanika", "Mechanika", "I", "intellect", field_group("C", 46), universe_field="ON 10", profession_field="ON 30"),
    skill_row("medycyna", "Medycyna", "I", "intellect", field_group("C", 51), universe_field="ON 11", profession_field="ON 31"),
    skill_row("odpornosc", "Odporność", "K", "brawn", field_group("C", 56), universe_field="ON 12", profession_field="ON 32"),
    skill_row("opanowanie", "Opanowanie", "P", "presence", field_group("C", 61), universe_field="ON 13", profession_field="ON 33"),
    skill_row("percepcja", "Percepcja", "S", "cunning", field_group("C", 66), universe_field="ON 14", profession_field="ON 34"),
    skill_row("pilotaz", "Pilotaż", "Z", "agility", field_group("C", 71), universe_field="ON 15", profession_field="ON 35"),
    skill_row("pojazdy_zalogowe", "Pojazdy załogowe", "I", "intellect", field_group("C", 76), universe_field="ON 16", profession_field="ON 36"),
    skill_row("prowadzenie_pojazdow", "Prowadzenie pojazdów", "Z", "agility", field_group("C", 81), universe_field="ON 17", profession_field="ON 37"),
    skill_row("sztuka_przetrwania", "Sztuka przetrwania", "S", "cunning", field_group("C", 86), universe_field="ON 18", profession_field="ON 38"),
    skill_row("ukrywanie_sie", "Ukrywanie się", "Z", "agility", field_group("C", 91), universe_field="ON 19", profession_field="ON 39"),
    skill_row("znajomosc_polswiatka", "Znajomość półświatka", "S", "cunning", field_group("C", 96), universe_field="ON 20", profession_field="ON 40"),
    skill_row("moc_boska", "Moc boska", "W", "willpower", field_group("A", 1), universe_field="ON 41", profession_field="ON 44"),
    skill_row("moc_pierwotna", "Moc pierwotna", "S", "cunning", field_group("A", 6), universe_field="ON 42", profession_field="ON 45"),
    skill_row("moc_tajemna", "Moc tajemna", "I", "intellect", field_group("A", 11), universe_field="ON 43", profession_field="ON 46"),
    skill_row("artyleria", "Artyleria", "Z", "agility", field_group("A", 16), universe_field="ON 47", profession_field="ON 55"),
    skill_row("bijatyka", "Bijatyka", "K", "brawn", field_group("A", 21), universe_field="ON 48", profession_field="ON 56"),
    skill_row("bron_biala", "Broń biała", "K", "brawn", field_group("A", 26), universe_field="ON 49", profession_field="ON 57"),
    skill_row("bron_biala_ciezka", "Broń biała (ciężka)", "K", "brawn", field_group("A", 31), universe_field="ON 50", profession_field="ON 58"),
    skill_row("bron_biala_lekka", "Broń biała (lekka)", "K", "brawn", field_group("A", 36), universe_field="ON 51", profession_field="ON 59"),
    skill_row("bron_dystansowa", "Broń dystansowa", "Z", "agility", field_group("A", 41), universe_field="ON 52", profession_field="ON 60"),
    skill_row("bron_dystansowa_ciezka", "Broń dystansowa (ciężka)", "Z", "agility", field_group("A", 46), universe_field="ON 53", profession_field="ON 61"),
    skill_row("bron_dystansowa_lekka", "Broń dystansowa (lekka)", "Z", "agility", field_group("A", 51), universe_field="ON 54", profession_field="ON 62"),
    skill_row("negocjacje", "Negocjacje", "P", "presence", field_group("A", 56), universe_field="ON 63", profession_field="ON 68"),
    skill_row("oszustwo", "Oszustwo", "S", "cunning", field_group("A", 61), universe_field="ON 64", profession_field="ON 69"),
    skill_row("przymuszanie", "Przymuszanie", "W", "willpower", field_group("A", 66), universe_field="ON 65", profession_field="ON 70"),
    skill_row("przywodztwo", "Przywództwo", "P", "presence", field_group("A", 71), universe_field="ON 66", profession_field="ON 71"),
    skill_row("urok_osobisty", "Urok osobisty", "P", "presence", field_group("A", 76), universe_field="ON 67", profession_field="ON 72"),
    skill_row("wiedza", "Wiedza", "I", "intellect", field_group("A", 81), universe_field="ON 73", profession_field="ON 77"),
    skill_row("wiedza_2", "Wiedza własna 1", "I", "intellect", field_group("A", 86), universe_field="ON 74", profession_field="ON 78", label_field="Text1", editable_label=True, editable_characteristic=True),
    skill_row("wiedza_3", "Wiedza własna 2", "I", "intellect", field_group("A", 91), universe_field="ON 75", profession_field="ON 79", label_field="Text3", editable_label=True, editable_characteristic=True),
    skill_row("wiedza_4", "Wiedza własna 3", "I", "intellect", field_group("A", 96), universe_field="ON 76", profession_field="ON 80", label_field="Text4", editable_label=True, editable_characteristic=True),
    skill_row("niestandardowa_1", "Umiejętność własna 1", "I", "intellect", field_group("E", 1), universe_field="ON 81", profession_field="ON 85", label_field="Text55", editable_label=True, editable_characteristic=True),
    skill_row("niestandardowa_2", "Umiejętność własna 2", "I", "intellect", field_group("E", 6), universe_field="ON 82", profession_field="ON 86", label_field="Text80", editable_label=True, editable_characteristic=True),
    skill_row("niestandardowa_3", "Umiejętność własna 3", "I", "intellect", field_group("E", 11), universe_field="ON 83", profession_field="ON 87", label_field="Text81", editable_label=True, editable_characteristic=True),
    skill_row("niestandardowa_4", "Umiejętność własna 4", "I", "intellect", field_group("E", 16), universe_field="ON 84", profession_field="ON 88", label_field="Text82", editable_label=True, editable_characteristic=True),
]


SKILL_ROWS_BY_SLUG: Final[dict[str, dict[str, object]]] = {row["slug"]: row for row in SKILL_ROWS}
SKILL_SLUGS: Final[list[str]] = [row["slug"] for row in SKILL_ROWS]
