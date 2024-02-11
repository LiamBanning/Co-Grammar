shape = range(1, 10)
number = 0
num = 5

for i in shape:
    if number == 5:
        num -= 1
        print("*" * num)
    elif i >= 1:
        number += 1
        print("*" * number)

# Initiates a loop that checks each iteration between a range of 1-10, the first condition checks to see if the iteration == 5, if not then
# checks to see if the iteration is >= 1, if so then +1 is added to a count and then moves onto the next iteration, each iteration is multiplied
# by the iteration count. Once the count reaches 5, then the first condition becomes true, and then the iteration count is decreased by 1.
# The range being set to 1 - 10 allows the iteration to be checked 10 times, allowing for 5 positive increments, and 5 negative increments.

        