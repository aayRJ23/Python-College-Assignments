def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def gcd_of_three(x, y, z):
    return gcd(x, gcd(y, z))

def calculate_gcd():
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        num3 = int(input("Enter third number: "))

        result = gcd_of_three(num1, num2, num3)
        print("The GCD of", num1, ",", num2, "and", num3, "is:", result)

    except ValueError:
        print("Please enter valid integers.")

calculate_gcd()  # Call the function to start the program
