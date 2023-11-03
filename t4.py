import sys

# Test Script 4
def main(string, arg1, arg2):
    print(f"Executing test4 (t4.py) with arguments: {string}, {arg1}, {arg2}")
    return "test4_success"

if __name__ == "__main__":
    string = sys.argv[1] if len(sys.argv) > 1 else ""
    arg1 = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    arg2 = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    result = main(string, arg1, arg2)
    print(result)

