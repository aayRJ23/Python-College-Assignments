num = int(input("Enter a number to calculate its factorial: "))
# Check if the number is negative
if num < 0:
        print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    # Calculate the factorial iteratively
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)