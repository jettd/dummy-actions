import sys

# Test Script 3
def main(arg1, arg2):
    print(f"Executing test3 (t3.py) with arguments: {arg1}, {arg2}")
    return "test3_success"

if __name__ == "__main__":
    arg1 = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    arg2 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    result = main(arg1, arg2)
    print(result)

