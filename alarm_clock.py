# Ask the user for the current time and the number of hours to wait.
currentTime = int(input("Enter current time (0-23): "))
waitHours = int(input("Enter hours to wait: "))

# Store the time values in a list and add them together.
timeValues = [currentTime, waitHours]
totalHours = 0

for hours in timeValues:
    totalHours += hours

# Calculate the alarm time using modulo division.
alarmTime = totalHours % 24

# Display the result.
print("Alarm will go off at:", alarmTime)
