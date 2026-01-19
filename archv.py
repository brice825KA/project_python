print("----Archive Text----")
text = input("Enter text: ")
split_text = text.split("|")
nombre = split_text[2].split(":")[1]
print("Nombre: ", float(nombre))
