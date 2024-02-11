# Visit the virual pub

int(input("""Welcome, what can I get you?
#1 beer
#2 soft drink
#3 water
        
Please enter 1, 2 or 3: """)) = drink_choice # Semantic error - expression should be on the right of an assignment (compilation error)

if drink_choice == 1  # Syntax error - if condition is missing a ':' (compilation error)
    age = int(input('How old are you? '))
    if age < 18: # Logical error - condition should check if age is >= 18
        print('Grab a beer, cheers mate!')
    else:
        print('You must be age 18 or over to have a beer, nice try! Grab a soft drink :)')
elif drink_choice == 2:
    soft_drinks = ['pepsi', 'pepsi max', 'lemonade', 'apple tango', 'orange tango']
    choice = int(input("""I have several options for you:
#1 pepsi
#2 pepsi max
#3 lemonade
#4 apple tango
#5 orange tango

Please enter 1, 2, 3, 4 or 5: """))
    while soft_drinks[choice] == soft_drinks[choice]: # Runtime error - infinite loop as condition never evaluates to False
        print(f'Enjoy your {soft_drinks[choice]}!')
elif drink_choice == 3:
    print('Treat yourself, you can get water at home!')
else:
    print('You have made an invalid selection, please try again.')
