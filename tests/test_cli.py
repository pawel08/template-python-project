"""Unit tests for the CLI module."""
import sys
import os
import pytest
from unittest.mock import patch

# Add the root directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli import main


def test_cli_addition():
    """Test the CLI with two numbers."""
    with patch('builtins.input', side_effect=['5', '3']):
        with patch('builtins.print') as mock_print:
            main()
            # Check that the result is printed
            calls = [str(call) for call in mock_print.call_args_list]
            assert any('8' in str(call) for call in calls)
