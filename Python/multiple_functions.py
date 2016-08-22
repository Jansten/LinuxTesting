# multiple_functions.py
# 2016-08-22, Michael Hannon
# Uses multiple functions together to calculate the overall cost of a trip
# This is an expanded program, based on one created during the codeCademy Python course

# Calculates the hotel cost, at $140/night
def hotel_cost(nights):
    return 140 * nights
    
# Calculates the plane ride cost depending on what city
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
# Calculates the rental car cost based on days, including two different 
def rental_car_cost(days):
    cost = days *40
    if days >= 7:
        cost = cost - 50
    elif days >= 3 and days < 7:
        cost = cost - 20
    return cost
    
# Calculate the entire trip cost, inlcuding extra spending money
def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    
# Return the total trip cost, based on user input
input_city = raw_input("Please enter the city: ")
input_days = int(raw_input("Please enter the number of days: "))
input_spending_money = int(raw_input("Please enter the amount of spending money: "))
print "The Total trip cost (in dollars) is: "
#print trip_cost("Los Angeles",5,600)
print trip_cost(input_city,input_days,input_spending_money)