"""Unit tests for the CLI module."""

import os
import sys
from unittest.mock import patch

# Ensure the root directory is in the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cli import main


def test_cli_addition():
    """Test the CLI with two numbers."""
    with patch("builtins.input", side_effect=["5", "3"]):
        with patch("builtins.print") as mock_print:
            main()
            # Check that the result is printed
            calls = [str(call) for call in mock_print.call_args_list]
            assert any("8" in str(call) for call in calls)
