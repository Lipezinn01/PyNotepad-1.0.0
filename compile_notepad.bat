@echo off
echo ========================================
echo  COMPILING NOTEPAD TO .EXE
echo ========================================
echo.

echo [1/3] Uninstalling the old PyInstaller...
python -m pip uninstall pyinstaller -y

echo.
echo [2/3] INSTALLING THE LATEST PYINSTALLER...
python -m pip install pyinstaller==5.13.2

echo.
echo [3/3] Compiling Notepad.py...
python -m PyInstaller --onefile --windowed --icon=image.ico --name="Notepad" notepad.py

echo.
echo ========================================
echo  OK!
echo ========================================
echo.
echo The .EXE file is located in: dist\Notepad.exe
echo.
echo OK!
echo.
pause
