import sys
from draw_rec import draw_rectangle
from count_occ import count_occ

def main():
    if len(sys.argv) == 1:
        return 84
    else:
        occ = count_occ(str(sys.argv[1]), str(sys.argv[2]))
        print(f"count: {occ}")
if __name__ == "__main__":
    main()
