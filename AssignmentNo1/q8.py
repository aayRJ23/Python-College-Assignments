# Take input from the user for the number of terms
n = int(input("Enter the number of terms for the Fibonacci series: "))

# Initialize the first two terms of the Fibonacci sequence
a, b = 0, 1

# Count to keep track of the number of terms printed
count = 0

# Check if the input is valid
if n <= 0:
    print("Please enter a positive integer.")
elif n == 1:
    print("Fibonacci series up to", n, "term:")
    print(a)
else:
    print("Fibonacci series up to", n, "terms:")
    while count < n:
        print(a, end=" ")
        # Update the Fibonacci sequence
        c = a + b
        # Update values for the next iteration
        a = b
        b = c
        count += 1
