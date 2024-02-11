import math
# Provides the user with the choice of selecting investment or bond option
print('''Investment - To calculate the amount of interest you'll earn on your investment
Bond       - To calculate the amount you will have to pay on a home loan''')
# Converts input into lowercase to ensure that the input is not case sensitive
user_input = input('Enter either \'investment\' or \'bond\' from the menu above to proceed: ').lower()


# Checks the input to see if input == 'investment', if it is, then propmpts user to input deposit amount, 
# yearly interest rate and the amount of years to invest. If input != 'investment', then this block is ignored
# and code jumps to line 28
if user_input == 'investment':
    deposit = float(input("How much are you depositing? ($): "))
    interest = float(input("Your interest rate (%): "))
    new_interest = interest / 100
    years = float(input("Number of years investing: "))
    
    # Prompts user to enter simple or compound interest, seperate calculations are done for either selection.
    type = input('Do you want \'simple\' or \'compound\' interest?: ').lower()
    if type == 'simple':
        total = round(deposit * (1 + new_interest * years), 2)
        print(f"Your total investment of ${deposit} at {interest}% over {years} years will return ${total}")
    elif type == 'compound':
        total = round(deposit *  math.pow((1 + new_interest), years), 2)
        print(f"Your total investment of ${deposit} at {interest}% over {years} years will return ${total}")
    else:
        print("Your input is invalid")

elif user_input == 'bond':
    house_value = float(input("What is your house's current value? ($): "))
    interest = float(input("Your interest rate (%): "))
    interest = interest / 100
    months = float(input("Number of months needed to repay the bond: "))
    monthly_interest = interest / 12
    repayment = round((monthly_interest * house_value) / (1 - (1 + monthly_interest) ** (-months)), 2)
    print(f"Your monthly repayment will be ${repayment}")
    
else:
    print("Your input is invalid")
