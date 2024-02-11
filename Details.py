#Get input for user's name
#Store inpout in variable called name
#Get input for user's age
#Store input in variable called age
#Get input for user's house number
#Store input in variable called house_number
#Get input for user's street name
#Store input in variable called street_name
#Use f-string to print out all variables

name = input("What is your name? ")
age = input(f"Hello {name}, how old are you? ")
house_number = input("What is your house number? ")
street_name = input(f"Finally, what street is number {house_number} on? ")
print(f"This is {name}, they are {age} years old and lives at {house_number} {street_name}")
