def fizzbuzz(number=(int)):
    for i in range(17):
        if i == 0:
            print("0")
        elif i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
