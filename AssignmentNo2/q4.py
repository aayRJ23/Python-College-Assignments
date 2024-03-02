def time_to_seconds(time_str):
    try:
        # Split the time string into hours, minutes, and seconds
        hours, minutes, seconds = map(int, time_str.split(':'))
        
        # Convert hours, minutes, and seconds to seconds
        total_seconds = hours * 3600 + minutes * 60 + seconds
        return total_seconds
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM:SS format.")

# Example usage:
time_str = input("Enter time in 24-hour format (HH:MM:SS): ")
seconds = time_to_seconds(time_str)
print(f"{time_str} is equal to {seconds} seconds.")
