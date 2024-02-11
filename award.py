cycling_time = int(input("What was your cycling time in minutes?: "))
swimming_time = int(input("What was your swimming time in minutes?: "))
running_time = int(input("What was your running time in minutes?: "))
total_time = cycling_time + swimming_time + running_time

if total_time <= 100:
    print(f"Your total time is {total_time} minutes, you have received the Provincial colours!")
elif total_time >= 101 and total_time <= 105:
    print(f"Your total time is {total_time} minutes, you have recieved the Provincial half colours!")
elif total_time >= 106 and total_time <= 110:
    print(f"Your total time is {total_time} minutes, you have recieved the Provincial Scroll!")
else:
    print(f"Your total time is {total_time} minutes, unfortunately you have recieved no award")
