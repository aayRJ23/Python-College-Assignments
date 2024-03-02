def repeat_string(string, times):
    
    if times <= 0:
        return ""
    else:
        return string * times

# Test the function
string_to_repeat = input("Enter the string you want to repeat: ")
repeat_times = int(input("Enter the number of times you want to repeat the string: "))

result = repeat_string(string_to_repeat, repeat_times)
print("Repeated string:", result)
