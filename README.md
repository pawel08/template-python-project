# Simple Python CLI Application

This project is a simple Python command-line interface (CLI) application that demonstrates the structure and organization of a Python project. It includes a CLI module, a logic module, and a set of tests to ensure the functionality of the application.

## Project Structure

```
simple-python-cli
├── src
│   ├── cli.py          # Command-line interface for the application
│   └── app
│       ├── __init__.py # Marks the directory as a Python package
│       └── core.py     # Core logic of the application
├── tests
│   ├── test_core.py    # Unit tests for the core logic
│   └── test_cli.py     # Unit tests for the CLI module
├── pyproject.toml      # Configuration file for dependencies and tools
├── requirements.txt     # Lists required Python packages
├── scripts
│   ├── create_venv.sh  # Script to create a virtual environment
│   ├── test.sh         # Script to run tests
│   ├── format_check.sh  # Script to check code formatting
│   └── lint.sh         # Script to run linter
├── .github
│   └── workflows
│       └── ci.yml      # CI workflow configuration
└── README.md           # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd simple-python-cli
   ```

2. Create a virtual environment and install dependencies:
   ```
   bash scripts/create_venv.sh
   ```

## Usage

To run the application, use the following command:
```
python src/cli.py
```

## Running Tests

To run the tests, execute:
```
bash scripts/test.sh
```

## Code Quality

This project uses `black` for code formatting and `pylint` for linting. You can check the formatting and linting by running:
```
bash scripts/format_check.sh
bash scripts/lint.sh
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.