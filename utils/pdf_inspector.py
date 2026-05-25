from __future__ import annotations

import json
from pathlib import Path

from pypdf import PdfReader


POLISH_MOJIBAKE_MAP = {
    "\u00cb\u2021": "\u0143",
    "\u00cb\u0165": "\u0118",
    "\u00cb\u2122": "\u015a",
    "\u00cb\u2020": "\u0106",
    "\u00cb\u203a": "\u017b",
}


def repair_text(value):
    if not isinstance(value, str):
        return value

    candidates = [value]
    for src_encoding, target_encoding in (("latin1", "utf-8"), ("cp1250", "utf-8"), ("cp1252", "utf-8")):
        try:
            candidates.append(value.encode(src_encoding).decode(target_encoding))
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue

    best = max(candidates, key=text_score)
    for source, target in POLISH_MOJIBAKE_MAP.items():
        best = best.replace(source, target)
    return best


def text_score(value: str) -> int:
    score = 0
    good_markers = "\u0105\u0107\u0119\u0142\u0144\u00f3\u015b\u017a\u017c\u0104\u0106\u0118\u0141\u0143\u00d3\u015a\u0179\u017b"
    bad_markers = "\u00c3\u00c4\u00c5\u00cb\u0139\u0102\u02c7\u02dd\u02d9\u02c6\u02db"
    score += sum(4 for char in value if char in good_markers)
    score -= sum(3 for char in value if char in bad_markers)
    return score


def make_json_safe(value):
    if isinstance(value, str):
        return repair_text(value)
    if isinstance(value, dict):
        return {str(key): make_json_safe(inner) for key, inner in value.items()}
    if isinstance(value, (list, tuple)):
        return [make_json_safe(item) for item in value]
    try:
        json.dumps(value)
        return value
    except TypeError:
        return repr(value)


def inspect_pdf_fields(pdf_path: Path, output_path: Path, verbose: bool = False) -> dict:
    reader = PdfReader(str(pdf_path))
    fields = reader.get_fields()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as stream:
        if not fields:
            stream.write("NO_FIELDS_FOUND\n")
            return {
                "ok": True,
                "editable": False,
                "fieldCount": 0,
                "outputPath": str(output_path),
                "pdfPath": str(pdf_path),
            }

        stream.write(f"Found {len(fields)} fields in {pdf_path}\n")
        for name, info in fields.items():
            safe_name = repair_text(name)
            safe_label = repair_text(info.get("/TU"))
            safe_value = repair_text(info.get("/V"))
            stream.write("=" * 60 + "\n")
            stream.write(f"FIELD: {safe_name}\n")
            stream.write(f"LABEL: {safe_label}\n")
            stream.write(f"TYPE:  {info.get('/FT')}\n")
            stream.write(f"VALUE: {safe_value}\n")
            if verbose:
                pretty = json.dumps(make_json_safe(info), indent=2, ensure_ascii=False)
                stream.write(pretty + "\n")

    return {
        "ok": True,
        "editable": True,
        "fieldCount": len(fields),
        "outputPath": str(output_path),
        "pdfPath": str(pdf_path),
    }
