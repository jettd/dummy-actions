import sys

# Test Script 6 (algorithm errors out in execution)
def main(illegal_string_arg):
    print(f"Executing test6 (t6.py) with argument: {illegal_string_arg}")
    raise ValueError("Illegal argument encountered")

if __name__ == "__main__":
    illegal_string_arg = sys.argv[1] if len(sys.argv) > 1 else ""
    main(illegal_string_arg)

