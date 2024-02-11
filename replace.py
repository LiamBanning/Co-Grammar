number = int(input("Please enter a number: "))
total = 0
count = 0
while number != -1:
    total += number
    count += 1
    number = int(input("Please enter a number: "))
print(total / count)
