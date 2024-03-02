# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is less than 2
if num < 2:
    is_prime = False
else:
    # Iterate from 2 to the square root of the number
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

# Display the result
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
