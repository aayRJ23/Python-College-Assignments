# Input the real and imaginary parts of the first complex number
real1 = float(input("Enter the real part of the first complex number: "))
imaginary1 = float(input("Enter the imaginary part of the first complex number: "))

# Input the real and imaginary parts of the second complex number
real2 = float(input("Enter the real part of the second complex number: "))
imaginary2 = float(input("Enter the imaginary part of the second complex number: "))

# Create complex numbers using the input values
complex_num1 = complex(real1, imaginary1)
complex_num2 = complex(real2, imaginary2)

# Addition of two complex numbers
addition_result = complex_num1 + complex_num2

# Subtraction of two complex numbers
subtraction_result = complex_num1 - complex_num2

# Display the results
print("Addition result:", addition_result)
print("Subtraction result:", subtraction_result)
