#!/bin/bash

# This script formats the code using black.
# It will automatically fix formatting issues.

echo "Formatting code with black..."

# Run black to format the code
black src tests scripts

if [ $? -eq 0 ]; then
    echo "Code formatted successfully."
else
    echo "Code formatting failed. Please check the errors above."
    exit 1
fi
