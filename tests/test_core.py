"""Unit tests for the core module."""
import pytest

from src.core import add_numbers


def test_add_numbers_positive():
    """Test adding two positive numbers."""
    result = add_numbers(5, 3)
    assert result == 8


def test_add_numbers_negative():
    """Test adding negative numbers."""
    result = add_numbers(-5, -3)
    assert result == -8


def test_add_numbers_mixed():
    """Test adding mixed positive and negative numbers."""
    result = add_numbers(10, -5)
    assert result == 5


def test_add_numbers_zero():
    """Test adding with zero."""
    result = add_numbers(5, 0)
    assert result == 5

