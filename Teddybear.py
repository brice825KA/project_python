import sys


def main():
    length = len(sys.argv)
    if length == 1:
        return 84
    for i in range(1, length):
        num = int(sys.argv[i])
        if sys.argv[1] > sys.argv[2]:
            return 84
        elif num % 9 == 0 and num % 10 == 0:
            print("TeddyBear")
        elif num % 9 == 0:
            print("Teddy")
        elif num % 10 == 0:
            print("Bear")
        else:
            print(sys.argv[i])


if __name__ == "__main__":
    main()
