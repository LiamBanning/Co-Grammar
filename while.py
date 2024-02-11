number = int(input("Please enter a number: "))
total = 0
count = 0
# Asks user to input a number, total tracks the sum of all numbers entered, count tracks the amount fo times a number has been entered.

while number != -1:
    total += number
    count += 1
    number = int(input("Please enter a number: "))
print(total / count)
# Runs a loops that will add the number to total, and add +1 to count, as long as the number entered is not -1.
# As long as the number entered is not -1, the user will be prompted to input another number.
# Once the loop has been broken - i.e when -1 is entered - the sum of all numbers entered is divided by the count of inputs and printed to the console,
# giving the average.
