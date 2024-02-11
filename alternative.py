# Takes a user input and stores in a variable
# Creates an empty list and sets position to 0, then for loop iterates between
# each character in the string, converts character to uppercase if the position
# number is even and adds to list, otherwise converts to lower case and apends to list.
# The list is then joined and printed to the console.
user_input = input("Please enter a string: ")
new_string = []
pos = 0
for i in user_input:
    if pos % 2 == 0:
        new_string.append(i.upper())
        pos += 1
    else:
        new_string.append(i.lower())
        pos += 1
new_string = "".join(new_string)
print(new_string)

# Same as the code above, however the input is split into individual words,
# which are then converted into upper case or lower case words respectively.
user_input = input("Please enter a string: ").split()
new_string = []
pos = 0
for i in user_input:
    if pos % 2 == 0:
        new_string.append(i.lower())
        pos += 1
    else:
        new_string.append(i.upper())
        pos += 1
new_string = " ".join(new_string)
print(new_string)