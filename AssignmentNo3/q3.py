def print_memory_location(input_string):
    print(f"Memory location of the string {input_string} : {id(input_string)}")

def main():
    user_input = input("Enter a string: ")
    print_memory_location(user_input)

if __name__ == "__main__":
    main()
