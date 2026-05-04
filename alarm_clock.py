# Ask the user for the current time and the number of hours to wait.
currentTime = int(input("Enter current time (0-23): "))
waitHours = int(input("Enter hours to wait: "))

# Calculate the alarm time using modulo division.
alarmTime = (currentTime + waitHours) % 24

# Display the result.
print("Alarm will go off at:", alarmTime)
