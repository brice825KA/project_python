print("----Analyse Text----")
text = input("Enter text: ")
caractere = list(text)
if caractere[0] == " " or caractere[len(caractere) - 1] == " ":
    caractere = caractere[1:-1]
for i in range(len(caractere)):
    caractere[i] = caractere[i].upper()
print("".join(caractere))
