from __future__ import annotations

import argparse
from pathlib import Path

from utils.pdf_inspector import inspect_pdf_fields


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inspect AcroForm fields in a PDF and print their names, labels, and types."
    )
    parser.add_argument(
        "--pdf",
        type=Path,
        default=Path("template") / "PL_-_ESGNS01PL-D01a_Character_Sheet.pdf",
        help="Path to the PDF file to inspect.",
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Print the full field dictionaries instead of a compact summary.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("output") / "pdf-fields.txt",
        help="Path to the text file that should receive the dump.",
    )
    args = parser.parse_args()
    inspect_pdf_fields(args.pdf, args.output, verbose=args.verbose)
    print(f"Wrote field dump to {args.output}")


if __name__ == "__main__":
    main()
