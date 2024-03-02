# Starting from 2 to 100, we will print even numbers
# We iterate over the range from 2 to 101 (101 is exclusive)
for num in range(2, 101):
    # Check if the number is even using the modulo operator
    if num % 2 == 0:
        # Print the even number
        print(num , end=",")
