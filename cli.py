import argparse
from src.core import some_function  # Replace with actual function(s) from core.py

def main():
    parser = argparse.ArgumentParser(description="Simple Python CLI Application")
    parser.add_argument('input', type=str, help='Input for the application')
    
    args = parser.parse_args()
    
    result = some_function(args.input)  # Replace with actual function call
    print(result)

if __name__ == "__main__":
    main()