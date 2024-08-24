@echo off
setlocal

:: Set the requirements file
set "REQUIREMENTS_FILE=requirements.txt"

:: Check if pip or pip3 is available
where pip3 >nul 2>&1
if %errorlevel% equ 0 (
    set "PIP_COMMAND=pip3"
) else (
    where pip >nul 2>&1
    if %errorlevel% equ 0 (
        set "PIP_COMMAND=pip"
    ) else (
        echo Neither pip nor pip3 found. Please install pip or pip3.
        exit /b 1
    )
)

:: Install packages from requirements.txt
if exist "%REQUIREMENTS_FILE%" (
    echo Installing packages from %REQUIREMENTS_FILE%...
    %PIP_COMMAND% install -r "%REQUIREMENTS_FILE%"
) else (
    echo %REQUIREMENTS_FILE% not found!
    exit /b 1
)

:: Start the Quart application
if exist "app.py" (
    echo Starting Quart application...
    python app.py
) else (
    echo app.py not found!
    exit /b 1
)

endlocal
