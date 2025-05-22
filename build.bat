@echo off
cd /d "%~dp0"

:: Always use py (not python) so we avoid path conflicts
set PY_CALL=py

:: STEP 1: Make sure pip is available
%PY_CALL% -m ensurepip --upgrade

:: STEP 2: Install pyinstaller just in case
%PY_CALL% -m pip install --upgrade pyinstaller

:: STEP 3: Manually run pyinstaller module
%PY_CALL% -m PyInstaller --onefile --noconsole main.pyw

:: STEP 4: Check if it worked
if exist dist\main.exe (
    echo.
    echo ✅ Build SUCCESSFUL! main.exe created in the "dist" folder.
) else (
    echo.
    echo ❌ Build FAILED. PyInstaller still couldn’t run.
)

pause
