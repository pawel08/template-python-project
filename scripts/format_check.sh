#!/bin/bash

# This script checks the formatting of the code using black.
# It will format the code and display any issues found.

# Run black to check formatting
black --check src tests cli.py

# Capture the exit status of the black command
if [ $? -ne 0 ]; then
    echo "Code formatting issues found. Please fix them before committing."
    exit 1
else
    echo "Code formatting is correct."
fi