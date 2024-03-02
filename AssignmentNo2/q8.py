def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: compute factorial(n) = n * factorial(n-1)
    else:
        return n * factorial(n - 1)

# Test the function
number = int(input("Enter a non-negative integer: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", number, "is", factorial(number))
