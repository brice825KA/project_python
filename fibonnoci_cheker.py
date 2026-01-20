import sys


def main():
    if len(sys.argv) != 2:
        return 84
    number = int(sys.argv[1])
    fibonacci(number)


def fibonacci(number=5):
    two = 0
    one = 1
    three = 0
    i = 0
    if number < 0:
        print("Error: Number must be positive")
        return 84
    elif number == 0 or number == 1:
        print("OK\n")
        return 0
    while i < number:
        three = two + one
        print(three, end=" ")
        one += 1
        two += 1
        three = one + three
        print(three)
        i += 1


if __name__ == "__main__":
    main()
