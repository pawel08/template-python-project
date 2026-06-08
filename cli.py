"""Command-line interface for the application."""
from src.core import add_numbers


def main():
    """Main entry point for the CLI."""
    print("Simple Addition Calculator")
    print("-" * 30)
    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        result = add_numbers(num1, num2)
        print(f"\n{num1} + {num2} = {result}")
    except ValueError:
        print("Error: Please enter valid numbers")


if __name__ == "__main__":
    main()
