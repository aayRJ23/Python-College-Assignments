# Define the number of rows for the pattern
rows = 5

# Iterate through each row
for i in range(1, rows + 1):
    # Print each number in the row 'i' times
    for j in range(i):
        print(i, end=" ")
    # Move to the next line after printing each row
    print()
