from __future__ import annotations

import re
from pathlib import Path


def sanitize_filename(name: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9_-]+", "-", name.strip().lower())
    value = value.strip("-")
    return value or "karta-postaci"


def ensure_template_exists(template_path: Path) -> None:
    if not template_path.exists():
        raise FileNotFoundError(
            f"PDF template not found: {template_path}. Update the template path or choose another file."
        )


def list_template_files(template_dir: Path) -> list[Path]:
    template_dir.mkdir(parents=True, exist_ok=True)
    return sorted(template_dir.glob("*.pdf"))


def resolve_single_template(template_dir: Path) -> Path:
    templates = list_template_files(template_dir)
    if not templates:
        raise FileNotFoundError(f"No PDF template found in {template_dir}.")
    candidate = templates[0]
    ensure_template_exists(candidate)
    return candidate


def inspect_output_path(base_dir: Path, template_path: Path) -> Path:
    return base_dir / "output" / f"{template_path.stem}-fields.txt"
