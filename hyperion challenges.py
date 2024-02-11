def get_num_freed_prisoners(cells):
  cells_inv = [0 if item == 1 else 1 for item in cells]

  freed_prisoners = 0
  current_pos = 0
  turn = 0

  while True:
    cells_ = cells if turn % 2 == 0 else cells_inv

    while current_pos < len(cells_) and not cells_[current_pos]:
      current_pos += 1    

    if current_pos >= len(cells_):
      break

    freed_prisoners += 1
    turn += 1
  return freed_prisoners

print(get_num_freed_prisoners([1, 1, 0, 0, 0, 1, 0]))


size = int(input('Please enter a number:'))

print()
print("Identity matrix") 
for row in range(0, size):
  for col in range(0, size):
    # Here end is used to stay in same line
    if (row == col):
      print("1 ", end=" ")
    else:
      print("0 ", end=" ")
  print()      

print()

print("Reverse Identity matrix") 
for row in range(0, size):
  for col in range(0, size):
    # Here end is used to stay in same line
    if (row == col):
      print("0 ", end=" ")
    else:
      print("1 ", end=" ")
  print()   


str = "You can have data without information, but you cannot have information without data."
str_lower = str.lower()
alphabet = list(map(chr, range(97, 123)))

for i in alphabet:
  frequency = {i: 0}
  for j in str_lower:
    if j in frequency.keys():
      frequency[i] += 1
  if frequency[i] != 0:
    print(f'{i} : {frequency[i]}')


bathroom_line = ['Amy', 'Bea', 'Clare', 'Dion', 'Eva']
print(bathroom_line)
jenny_joins = bathroom_line.insert(0, 'Jenny')
print(bathroom_line)
bea_leaves = bathroom_line.remove('Bea')
print(bathroom_line)
alice_joins = bathroom_line.append('Alice')
print(bathroom_line)


hour = int(input("What hour is it? Enter a number 0-23:"))
guard = bool(input("Is the night guard on duty? Enter True or False:"))

if(hour in range(7,18) or guard == True):
  print("You're in!")
else:
  print("You're locked out!")


num_list = []
num = input("Please enter a number:")

while(num != '-1'):
  num_list.append(int(num))
  num = input("Please enter a number:")
  
average = sum(num_list) / len(num_list)

print(average)


name = input("Please enter your name:")
email_address = input("Please enter your email address:")

print(f"Hi {name}! We will be contacting you shortly at {email_address}")

animals = ['dog', 'cat', 'raccoon', 'lizard']
print(animals)
remove_animal2 = animals.remove('cat')
print(animals)
add_cheetah = animals.append('Cheetah')
print(animals)
remove_cheetah = animals.remove('Cheetah')
print(animals)

num = 1
while num < 11:
  print(num)
  num += 1


chosen_num = input("Please enter a number:")

if(int(chosen_num) % 2 == 0):
  print("fizz")
else:
  print("buzz")


string = "I!am!a!coding!genius!"
replaced_str = string.replace("!"," ")
print(replaced_str[::1])


word = input("Please enter a 6 letter word:")
reverse = word[::-1]
print("This is the word backwards: " + reverse)


weight = input("Please enter your weight:")
height = input("Please enter your height:")
bmi = int(weight) / int(height)**2
print("Your BMI is: " + str(bmi))


monthly_savings = (1250 - (650 + 175)) * 0.25
total = monthly_savings * 3

print("Amount to save each month: " + str(monthly_savings))
print("Total by December: " + str(total))