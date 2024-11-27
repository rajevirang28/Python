input_string = str(input("Enter the word:"))
reversed_string = ""

for char in input_string:
    reversed_string = char + reversed_string
print(reversed_string)