print("---ANALYSE TEXTE---")
text = str(input("Enter the texte: ").lower)
voyelle = "aeiouy"
count_voy = 0
count_word = 0
count_cons = 0

for i in range(len(text)):
    for j in range(len(voyelle)):
        if text[i] == voyelle[i]:
            count_voy += 1
        else:
            count_cons += 1
    if text[i] == " ":
        count_word += 1
print("count_word: ", count_word, "count_voy: ", count_voy, "count_cons: ", count_cons)
