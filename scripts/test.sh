#!/bin/bash

# This script runs the tests for the project using pytest.

# Activate the virtual environment
source venv/bin/activate

# Run the tests
pytest tests/ --maxfail=1 --disable-warnings -q

# Deactivate the virtual environment
deactivate