import sys
from FizzBuzz import fizzbuzz

def main():
    if len(sys.argv) == 1:
        return 84
    else:
        fizzbuzz(int(sys.argv[1]))
if __name__ == "__main__":
    main()
