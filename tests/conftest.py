"""Pytest configuration and fixtures."""

import os
import sys

# Add the root directory to Python path for test discovery
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
