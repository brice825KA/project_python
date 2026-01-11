import sys
from FizzBuzz import fizzbuzz
from table_mul import multiple_table

def main():
    if len(sys.argv) == 1:
        return 84
    else:
        multiple_table(int(sys.argv[1]))
if __name__ == "__main__":
    main()
