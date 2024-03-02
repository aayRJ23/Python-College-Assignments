def get_month(date_str):
    # Split the date string into day, month, and year
    day, month, year = map(int, date_str.split(':'))

    # Define a list of months
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Check if the month is within the valid range
    if 1 <= month <= 12:
        return months[month - 1]
    else:
        return "Invalid month"

# Main function
def main():
    date_input = input("Enter the date in dd:mm:yy format: ")
    month = get_month(date_input)
    print("The month is:", month)

if __name__ == "__main__":
    main()
