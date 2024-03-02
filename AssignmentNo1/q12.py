# Take input from the user
day_number = int(input("Enter a number (1-7) to represent a day of the week: "))

# Define a list to map day numbers to day names
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Check if the input is valid (between 1 and 7)
if 1 <= day_number <= 7:
    # Print the corresponding day using the list
    print("The day corresponding to number", day_number, "is", days_of_week[day_number - 1])
else:
    print("Invalid input. Please enter a number between 1 and 7.")
