#!/bin/bash

# This script runs the tests for the project using pytest.

# Run the tests from the root directory
pytest tests/ --maxfail=1 --disable-warnings -v
