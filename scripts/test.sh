#!/bin/bash

# This script runs the tests for the project using pytest.

# Run the tests from the root directory
pytest tests/ -v --tb=short
