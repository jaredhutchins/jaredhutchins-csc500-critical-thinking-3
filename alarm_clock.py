# Ask the user for the current time and the number of hours to wait.
current_time = int(input("Enter current time (0-23): "))
wait_hours = int(input("Enter hours to wait: "))

# Store the time values in a list and add them together.
time_values = [current_time, wait_hours]
total_hours = 0

for hours in time_values:
    total_hours += hours

# Calculate the alarm time using modulo division.
alarm_time = total_hours % 24

# Display the result.
print("Alarm will go off at:", alarm_time)
