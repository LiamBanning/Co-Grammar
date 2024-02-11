# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Sytanx error, string variable not saved in parenthesis
animal_type = "cub"
number_of_teeth = 16

full_spec = print(f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth") # Logical error, 
# variables are located in the wrong places in the string. Also has not been formatted as an f-string
# meaning that the variables will not be inserted into the string when printed.
 #Syntax error, print statement not wrapped in parenthesis
