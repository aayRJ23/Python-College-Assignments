# Global variable
global_var = 10

def modify_global_variable():
    global global_var
    print("Inside the function, before modification: global_var =", global_var)
    
    # Modifying the global variable
    global_var = 20
    
    print("Inside the function, after modification: global_var =", global_var)

# Call the function
modify_global_variable()

# Print the global variable outside the function
print("Outside the function: global_var =", global_var)
