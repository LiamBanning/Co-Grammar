# Visit the virual pub

drink_choice = int(input("""Welcome, what can I get you?
#1 beer
#2 soft drink
#3 water
        
Please enter 1, 2 or 3: """))

if drink_choice == 1:
    age = int(input('How old are you? '))
    if age < 18: # condition should check if age is >= 18
        print('Grab a beer, cheers mate!')
    else:
        print('You must be age 18 or over to have a beer, nice try! Grab a soft drink :)')
elif drink_choice == 2:
    soft_drinks = ['lemonade', 'orange tango', 'apple tango', 'pepsi', 'pepsi max'] # list order doesn't match selection menu order
    choice = int(input("""I have several options for you:
#1 pepsi
#2 pepsi max
#3 lemonade
#4 apple tango
#5 orange tango

Please enter 1, 2, 3, 4 or 5: """))
    print(f'Enjoy your {soft_drinks[choice]}!') # prints incorrect soft drink choice
elif drink_choice == 3:
    print('Treat yourself, you can get water at home!')
else:
    print('You have made an invalid selection, please try again.')
