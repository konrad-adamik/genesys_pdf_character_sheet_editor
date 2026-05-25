from __future__ import annotations

import io
import json
from pathlib import Path

from flask import Flask, jsonify, request, send_file, send_from_directory

from utils.pdf_form import build_filled_pdf_bytes, normalize_character_data
from utils.pdf_inspector import inspect_pdf_fields
from utils.template_manager import (
    inspect_output_path,
    list_template_files,
    resolve_single_template,
    sanitize_filename,
)

BASE_DIR = Path(__file__).resolve().parent
HTML_DIR = BASE_DIR / "html"
TEMPLATE_DIR = BASE_DIR / "template"

app = Flask(__name__, static_folder=str(BASE_DIR), static_url_path="")


@app.get("/")
def index():
    return send_from_directory(HTML_DIR, "index.html")


@app.get("/api/health")
def health():
    templates = list_template_files(TEMPLATE_DIR)
    template_path = str(templates[0]) if templates else ""
    return jsonify(
        {
            "ok": True,
            "templateExists": bool(templates),
            "templatePath": template_path,
            "templateCount": len(templates),
        }
    )

@app.post("/api/inspect-template")
def inspect_template():
    try:
        template_path = resolve_single_template(TEMPLATE_DIR)
        result = inspect_pdf_fields(
            template_path,
            inspect_output_path(BASE_DIR, template_path),
            verbose=False,
        )
        result["templateName"] = template_path.name
        return jsonify(result)
    except FileNotFoundError as error:
        return jsonify({"ok": False, "editable": False, "error": str(error)}), 400
    except Exception as error:  # pragma: no cover
        return jsonify({"ok": False, "editable": False, "error": f"Template inspection failed: {error}"}), 500


@app.post("/api/generate-pdf")
def generate_pdf():
    try:
        payload = request.get_json(force=True) or {}
        character = normalize_character_data(payload.get("character", payload))
        debug_grid = bool(payload.get("debugGrid", False))
        template_path = resolve_single_template(TEMPLATE_DIR)
        pdf_bytes = build_filled_pdf_bytes(character, template_path, debug_grid=debug_grid)
        filename = sanitize_filename(character.get("name", "karta-postaci")) + ".pdf"
        return send_file(
            io.BytesIO(pdf_bytes),
            mimetype="application/pdf",
            as_attachment=True,
            download_name=filename,
        )
    except FileNotFoundError as error:
        return jsonify({"error": str(error)}), 400
    except Exception as error:  # pragma: no cover
        return jsonify({"error": f"PDF generation failed: {error}"}), 500


@app.post("/api/save-json")
def save_json():
    try:
        payload = request.get_json(force=True) or {}
        character = payload.get("character", payload)
        normalized = normalize_character_data(character)
        output_dir = BASE_DIR / "characters"
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = sanitize_filename(normalized.get("name", "karta-postaci")) + ".json"
        output_path = output_dir / filename
        with output_path.open("w", encoding="utf-8") as stream:
            json.dump(normalized, stream, indent=2, ensure_ascii=False)
        return jsonify({"ok": True, "path": str(output_path), "filename": filename})
    except Exception as error:  # pragma: no cover
        return jsonify({"error": f"JSON save failed: {error}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
