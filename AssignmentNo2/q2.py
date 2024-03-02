def swap_numbers(num1, num2):
    temp = num1
    num1 = num2
    num2 = temp
    return num1, num2

# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Before swapping:")
print("First number:", num1)
print("Second number:", num2)

# Calling the function to swap numbers
num1, num2 = swap_numbers(num1, num2)

print("After swapping:")
print("First number:", num1)
print("Second number:", num2)
