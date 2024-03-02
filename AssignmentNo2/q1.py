def check_relation(num1, num2):
    if num1 > num2:
        return f"{num1} is greater than {num2}"
    elif num1 < num2:
        return f"{num1} is less than {num2}"
    else:
        return f"{num1} is equal to {num2}"

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function and display the result
result = check_relation(num1, num2)
print(result)