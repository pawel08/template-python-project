#!/bin/bash

# Create a virtual environment in the 'venv' directory
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the required dependencies
pip install -r requirements.txt

