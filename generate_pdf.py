from __future__ import annotations

import argparse
from pathlib import Path

from utils.pdf_form import build_filled_pdf_bytes, load_character


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fill the Genesys PDF form directly from JSON using the PDF's existing form fields."
    )
    parser.add_argument("character_json", type=Path, help="Path to the source character JSON file.")
    parser.add_argument(
        "--template",
        type=Path,
        default=Path("template") / "PL_-_ESGNS01PL-D01a_Character_Sheet.pdf",
        help="Path to the original PDF template.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output") / "character-sheet.pdf",
        help="Where the filled PDF should be written.",
    )
    args = parser.parse_args()

    data = load_character(args.character_json)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    pdf_bytes = build_filled_pdf_bytes(data, args.template)
    with args.output.open("wb") as stream:
        stream.write(pdf_bytes)
    print(f"Generated {args.output}")


if __name__ == "__main__":
    main()
