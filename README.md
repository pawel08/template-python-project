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

## Quick Start

### Prerequisites
- Python 3.8 or higher
- bash or compatible shell

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd simple-python-cli
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   bash scripts/create_venv.sh
   ```

## Usage

To run the application, use the following command:
```bash
python src/cli.py
```

## Development & Code Quality

### Running Tests

Execute the test suite:
```bash
bash scripts/test.sh
```

This runs all unit tests in the `tests/` directory using pytest with warnings disabled.

### Code Formatting

To automatically format your code using black:
```bash
bash scripts/format.sh
```

To check if code is properly formatted (without making changes):
```bash
bash scripts/format_check.sh
```

### Linting

To analyze code quality and style issues using pylint:
```bash
bash scripts/lint.sh
```

### Clean Repository

To remove cache files, build artifacts, and temporary files:
```bash
bash scripts/clean.sh
```

## Continuous Integration (CI)

### Pipeline Overview

This project includes an automated CI pipeline using GitHub Actions (`.github/workflows/python-app.yml`). The pipeline is triggered on:
- **Push** to `main`, `master`, or `develop` branches
- **Pull Request** to `main` or `master` branches

### What the Pipeline Checks

The CI pipeline automatically runs the following checks in order:

1. **Setup**: Checks out code and sets up Python 3.12
2. **Dependencies**: Creates a virtual environment and installs required packages
3. **Format Check**: Validates that code follows Black formatting standards (line-length: 88)
4. **Linting**: Checks code quality using Pylint
5. **Tests**: Runs the complete test suite using Pytest

If any step fails, the pipeline will fail and prevent merging of pull requests. All checks must pass for CI to succeed.

### Monitoring CI

You can monitor your CI pipeline:
- Go to the **Actions** tab in your GitHub repository
- View build logs and results for each step
- Failed checks show specific errors that need to be fixed locally

