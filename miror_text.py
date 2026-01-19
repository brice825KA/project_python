print("----Mirror of Raison----")
string_one = input("Enter test: ")
string_two = list(string_one)
string_three = string_two
string_two.reverse()
print("".join(string_two))
print("".join(string_one))
if string_two == string_one:
    print("Palidrome\n")
else:
    print("Not a Palindrome\n")
