#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    result = 0
    for x in range(count):
        result += int(sys.argv[x + 1])
    print(result)
