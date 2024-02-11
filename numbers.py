print("Welcome to the error program") #Syntax error - no parenthesis on print statement
print("\n") # Syntax error - incorrect indentation and missign parenthesis

# Variables declaring the user's age, casting the str to an int, and printing the result
age = 24 #Syntax error, == comparative operator used instead of assignment operator, also has incorrect indentation, also a runtime error
# because a string cannot be cast into an integer if there are non-numerical characters present. There is also
# a logical error present, since there is no need for a seperate variable to cast the str to int once the
# age variable has been changed to an int.
print(f"I'm {age} years old.") # Syntax error, incorrect indentation. Also a runtime error since a str cannot
# be concatenated to an int

# Variables declaring additional years and printing the total years of age
years_from_now = 3.5 # Logical error, gives incorrect output for total_months, also should be stored as float, not string
total_years = age + years_from_now

print(f"The total number of years: {total_years}") #Syntax error, no parenthesis on print statement, also a runtime error since
# there is no variable named answer_years, also a runtime error due to trying to concatenate a str to an int

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years * 12 # Runtime error, non-assigned variable used
print(f"In 3 years and 6 months, I'll be {total_months} months old") # Syntax error, print not in parenthesis,
# also a runtime error due to trying to concatenate str to int

#HINT, 330 months is the correct answer