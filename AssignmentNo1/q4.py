# Sample list (you can modify it with your own list)
num_list = [15, 20, 30, 45, 50, 60, 75, 80]

# Iterate through the list and display numbers divisible by 10
print("Numbers divisible by 10:")
for num in num_list:
    if num % 10 == 0:
        print(num , end=",")
