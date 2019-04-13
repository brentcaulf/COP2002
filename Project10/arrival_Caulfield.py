#!/usr/bin/env python3

from datetime import datetime, timedelta, time

#prompts user for departure date and time then converts them into a datetime and returns it
def get_departure_datetime():
    #gets and validates departure date
    while True:
        date_str = input("Estimated date of departure (YYYY-MM-DD): ")
        try:
            departure_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")
            continue
        break
    #gets and validates departure time
    while True:
        time_str = input("Estimated time of departure (HH:MM AM/PM): ")
        #splits the string into a list
        time_list = time_str.split()
        try:
            #gets the am or pm string from list
            am_pm_str = time_list[1].upper()
        except:
            print("Invalid time entry. Please try again.")
            continue
        #creates a time by splitting the user inputed hour and min into strings
        try:
            if am_pm_str == "AM":
                hour_min = time_list[0].split(":")        
                departure_time = time(int(hour_min[0]), int(hour_min[1]))
                break
            #if its PM, adds 12 to the hour int
            elif am_pm_str == "PM":
                hour_min = time_list[0].split(":")
                departure_time = time(int(hour_min[0]) + 12, int(hour_min[1]))
                break
            else:
                print("Invalid entry please enter AM or PM")
                continue
        except:
            print("Invalid time entry. Please try again.")
            continue
    #creates departure datetime using departure_date and departure_time datatime objects
    departure_datetime = datetime(departure_date.year, departure_date.month, departure_date.day, departure_time.hour, departure_time.minute)

    return departure_datetime

#gets and returns a valid mile entry from user
def get_miles():
    while True:                
        try:
            miles = int(input("Enter miles: "))
        except ValueError:
            print("Invalid entry, please enter a integer.")
            continue
        break

    return miles

#gets and returns a valid miles per hour entry from user
def get_mph():
    while True:                
        try:
            mph = int(input("Enter miles per hour: "))
        except ValueError:
            print("Invalid entry, please enter a integer.")
            continue
        break

    return mph

#calculates the travel time using miles and mph then returns a timedelta called travel_time
def calculate_travel_time(miles, mph):
    travel_hours = int(miles / mph)    
    
    travel_minutes = ((miles / mph) - travel_hours) * 60   
    
    travel_time = timedelta(hours=travel_hours, minutes=travel_minutes)

    print()
    print("Estimated travel time")
    print("Hours: ", travel_hours)
    print("Minutes: ", "{:.2f}".format(travel_minutes))
    
    return travel_time

#calculates and returns the arrival date time
def calculate_arrival_datetime(departure_datetime, travel_time):
    arrival_datetime = departure_datetime + travel_time

    return arrival_datetime
    
#main function
def main():
    print("Arrival Time Estimator")
    print()

    #start main program loop
    choice = "y"
    while choice.lower() == "y":
        #gets user input
        departure_datetime = get_departure_datetime()
        miles = get_miles()
        mph = get_mph()

        #calculates the travel time and arrival datetime
        travel_time = calculate_travel_time(miles, mph)
        arrival_datetime = calculate_arrival_datetime(departure_datetime, travel_time)

        #print results
        print("Estimated date of arrival: ", arrival_datetime.strftime("%Y-%m-%d"))
        print("Estimated time of arrival: ", arrival_datetime.strftime("%I:%M %p"))
        print()

        #check to see if user wants to do another calculation
        choice = input("Continue? (y/n): ")
        while (choice != "y" and choice != "n"):
            print("Please enter y or n")
            choice = input("Continue? (y/n): ")
        
        print()

if __name__ == "__main__":
    main()
