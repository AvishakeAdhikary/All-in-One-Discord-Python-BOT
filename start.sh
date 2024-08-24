#!/bin/bash

# Set the requirements file
REQUIREMENTS_FILE="requirements.txt"

# Check if pip or pip3 is available
if command -v pip3 > /dev/null 2>&1; then
    PIP_COMMAND="pip3"
elif command -v pip > /dev/null 2>&1; then
    PIP_COMMAND="pip"
else
    echo "Neither pip nor pip3 found. Please install pip or pip3."
    exit 1
fi

# Install packages from requirements.txt
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing packages from $REQUIREMENTS_FILE..."
    $PIP_COMMAND install -r $REQUIREMENTS_FILE
else
    echo "$REQUIREMENTS_FILE not found!"
    exit 1
fi

# Start the Quart application
if [ -f "app.py" ]; then
    echo "Starting Quart application..."
    python app.py
else
    echo "app.py not found!"
    exit 1
fi
