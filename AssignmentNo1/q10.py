# Take input from the user
num = int(input("Enter a number: "))

# Store a copy of the original number
original_num = num

# Initialize variables to store the reversed number and calculate its length
reversed_num = 0
temp_num = num
num_length = 0

# Calculate the length of the number
while temp_num > 0:
    temp_num //= 10
    num_length += 1

# Reverse the number
while num > 0:
    digit = num % 10
    reversed_num = reversed_num*10 + digit
    num //= 10

# Check if the original number is equal to the reversed number
if original_num == reversed_num:
    print(original_num, "is a palindrome")
else:
    print(original_num, "is not a palindrome")
