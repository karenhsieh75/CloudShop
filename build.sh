#!/bin/bash

echo "Building CloudShop CLI..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed or not in PATH"
    echo "Please install Python from https://www.python.org/downloads/"
    exit 1
fi

# Check if SQLite is installed
if ! command -v sqlite3 &> /dev/null; then
    echo "Error: SQLite is not installed or not in PATH"
    echo "Please install SQLite from https://www.sqlite.org/download.html"
    exit 1
fi

# Check if main.py exists
if [ ! -f "main.py" ]; then
    echo "Error: main.py not found!"
    exit 1
fi

echo "Build successful!"