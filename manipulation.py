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



        