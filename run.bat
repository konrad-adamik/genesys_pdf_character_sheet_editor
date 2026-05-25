@echo off
REM Simple Windows launcher for Genesys PDF Character Sheet Editor
REM Creates/uses a virtualenv, installs requirements, starts the Flask server, and waits for it to respond.

SETLOCAL

echo Checking for Python...
where python >nul 2>&1 || (
  echo Python not found. Install Python 3.8+ and add it to PATH.
  pause
  exit /b 1
)

if not exist venv (
  echo Creating virtual environment...
  python -m venv venv || (
    echo Failed to create virtual environment.
    pause
    exit /b 1
  )
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing required packages...
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt

echo Starting Flask server in a new terminal window...
start "Genesys Server" cmd /k "call venv\Scripts\activate.bat && python app.py"

echo Waiting for the server to become ready...
set MAX_TRIES=20
for /L %%i in (1,1,%MAX_TRIES%) do (
  powershell -NoProfile -Command "try { Invoke-WebRequest -UseBasicParsing -Uri 'http://127.0.0.1:5000/api/health' -TimeoutSec 2 | Out-Null; exit 0 } catch { exit 1 }"
  if not errorlevel 1 (
    goto server_ready
  )
  echo Waiting... %%i/%MAX_TRIES%
  timeout /t 1 >nul
)
echo Server did not start in %MAX_TRIES% seconds. Check the server window for errors.
pause
exit /b 1

:server_ready
echo Server is ready.
start "" "http://127.0.0.1:5000/"
echo Press any key to close this launcher window.
pause
ENDLOCAL
