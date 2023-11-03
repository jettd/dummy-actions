import sys

# Test Script 2
def main(arg1):
    print(f"Executing test2 (t2.py) with argument: {arg1}")
    return "test2_success"

if __name__ == "__main__":
    arg1 = sys.argv[1] if len(sys.argv) > 1 else ""
    result = main(arg1)
    print(result)

