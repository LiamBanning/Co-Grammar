# Function that taakes a standard daily hotel charge and multiplies by the inputted number of days
def hotel_cost (num_nights):
    daily_rate = 120
    cost = num_nights * daily_rate
    return cost

# Function that creates a variable for flight cost for the relevant cities,
# If if a city is not within the function, an error message is displayed.
def plane_cost (city_flights):
    if city_flights == "copenhagen":
        flight_cost = 115
    elif city_flights == "madrid":
        flight_cost = 146
    elif city_flights == "rome":
        flight_cost = 170
    else:
        print("Sorry, we do not fly to this destination.")
    return flight_cost


# Function that takes the amount of rental days and multiplies it by a standard daily rental fee
def car_rental (rental_days):
    daily_car = 50
    car_cost = rental_days * daily_car
    return car_cost

# Function that takes all other functions as arguments, and adds the returned values together.
def holiday_cost (hotel_cost, plane_cost, car_rental):
   total_cost = hotel_cost + plane_cost + car_rental
   return total_cost

# Asks for user input for city they are flying to, number of nights staying, car rental days required
city_flights = input("What city are you flying to?: ").lower()
num_nights = int(input("How many nights are you staying?: "))
rental_days = int(input("How many days do you require for car hire?: "))

# Calls the holiday cost function and prints out the returned value.
print(f"Your total cost for this holiday will be ${holiday_cost(car_rental(rental_days), plane_cost(city_flights), hotel_cost(num_nights))}")
