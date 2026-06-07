import subprocess
import sys
import click

@click.command()
@click.argument('arg1')
def main(arg1):
    """Main entry point for the CLI."""
    click.echo(f'You passed the argument: {arg1}')

if __name__ == '__main__':
    main()

# Test cases for the CLI module
import pytest
from click.testing import CliRunner
from src.cli import main

def test_cli():
    runner = CliRunner()
    result = runner.invoke(main, ['test_argument'])
    assert result.exit_code == 0
    assert 'You passed the argument: test_argument' in result.output