# Different Types of conditional statement are:
# if 
# elif
# nested elif
# elif ladder 
   # EXAMPLE OF CONDITIONAL OPERATOR USING TIME MODULE
import time
print("Current Year is :")
PresentYear = time.strftime("%Y-%B(%m)-%A")
print(PresentYear)

PreTime = time.strftime("%I:%M:%S %p")  # Fixed the time format
print("Current Time:", PreTime)
x = time.strftime("%I %p")  # Get hour in 12-hour format with AM/PM

if x == "12 AM":
    print("Good Night sir!")
elif "6 AM" <= x <= "11 AM":  # Between 6 AM and 11 AM
    print("Good Morning sir!")
elif "12 PM" <= x <= "5 PM":  # Between 12 PM and 5 PM
    print("Good Afternoon sir!")
elif "6 PM" <= x <= "11 PM":  # Between 6 PM and 11 PM
    print("Good Evening sir!")
else:
    print("Hello sir!")