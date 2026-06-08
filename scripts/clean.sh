#!/bin/bash

# This script cleans the repository of unnecessary files and directories.

echo "Cleaning repository..."

# Remove Python cache directories
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
echo "✓ Removed __pycache__ directories"

# Remove Python egg info directories
find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null
echo "✓ Removed *.egg-info directories"

# Remove pytest cache
rm -rf .pytest_cache 2>/dev/null
echo "✓ Removed .pytest_cache"

# Remove coverage reports
rm -rf .coverage htmlcov 2>/dev/null
echo "✓ Removed coverage reports"

# Remove mypy cache (if present)
rm -rf .mypy_cache 2>/dev/null
echo "✓ Removed .mypy_cache"

# Remove build artifacts
rm -rf build dist 2>/dev/null
echo "✓ Removed build artifacts"

# Remove virtual environment (optional - comment out if you want to keep it)
# rm -rf venv 2>/dev/null
# echo "✓ Removed venv directory"

echo "Repository cleaned successfully."
