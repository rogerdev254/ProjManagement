"""Tests for the `project_management` package."""
import pytest
from projectmanagement import notebook


def test_convert(capsys):
    """Test Correct name argument prints """
    notebook.convert('Rog')
    captured = capsys.readouterr()
    assert 'Rog' in captured.out
