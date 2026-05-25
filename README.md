# Genesys PDF Character Sheet Editor

## Requirements
- Python 3.8 or newer
- Windows only for `run.bat` launcher

## Run on Windows
1. Open the project folder.
2. Double-click `run.bat` or run it in a terminal:
   ```bat
   run.bat
   ```
3. The script will create `venv`, install dependencies, start the Flask server, wait for it to be ready, and open the browser.

## Manual run
If you want to run it manually:
```bat
python -m venv venv
venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000/` in your browser.
