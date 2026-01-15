import random

print("GAME RANDOM")
ale = random.randint(1, 100)
i = 1
while i <= 3:
    inmp = int(input("Entry a number: "))
    if inmp == ale:
        print("Number found")
        break
    elif inmp < ale:
        print("plus grand")
    else:
        print("plus petit")
    if i == 3 and inmp != ale:
        print("Number not found\n")
        break
    i += 1
