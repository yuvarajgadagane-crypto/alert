@echo off
title Student Sleep & Fall Alert System
color 0B
echo =====================================================================
echo        STUDENT SLEEP & FALL ALERT SYSTEM — LAUNCHER
echo =====================================================================
echo.
echo [1/2] Checking Python environment...
python --version >nul 2>&1
if %ERRORLEVEL% equ 0 (
    echo [OK] Python is available. Starting local server...
    echo.
    echo [2/2] Opening web application in your default browser...
    echo       URL: http://localhost:8000/index.html
    echo.
    echo Leave this window open while using the application.
    echo Close this window or press Ctrl+C to terminate.
    python server.py
) else (
    echo [WARNING] Python was not found in PATH.
    echo Launching index.html directly in your default browser...
    start "" "index.html"
)
pause
