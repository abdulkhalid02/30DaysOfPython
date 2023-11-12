time = int(input("Enter the 24hours time of a day:"))

if time >= 0 and time <= 5:
    print("Night")
elif time >= 6 and time <= 11:
    print("Morning")
elif time >= 12 and time <= 17:
    print("Afternoon")
elif time >= 18 and time <= 20:
    print("Evening")
else:
    print("Invalid")
