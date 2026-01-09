def draw_rectangle(a = 5, b = 4):
    i = 1
    square = 0
    while i <= a:
        j = 0
        ligne = ""
        while j < b:
            print("*", end="")
            j += 1
        i += 1
        print()
    square = a * b
    return square
