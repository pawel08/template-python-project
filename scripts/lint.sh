#!/bin/bash

# Run pylint on the src and tests directories
pylint src tests

# Check if pylint ran successfully
if [ $? -ne 0 ]; then
    echo "Linting failed. Please fix the issues above."
    exit 1
else
    echo "Linting passed!"
fi