# Take input from the user
num = int(input("Enter a number: "))

# Copy the number to calculate its length
temp_num = num

# Calculate the length of the number
num_length = 0
while temp_num > 0:
    num_length += 1
    temp_num //= 10

# Calculate the sum of digits raised to the power of num_length
temp_num = num
sum_of_digits = 0
while temp_num > 0:
    digit = temp_num % 10
    sum_of_digits += digit ** num_length
    temp_num //= 10

# Check if the number is an Armstrong number
if num == sum_of_digits:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
