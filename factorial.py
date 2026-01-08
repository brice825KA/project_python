def factorial(a = 5):
    i = 0
    count = 1

    if a == 0:
        return 1
    elif a < 0 or a >= 13:
        return 0
    else:
        while a >= 1:
          count = count * a
          a -= 1
    return count
