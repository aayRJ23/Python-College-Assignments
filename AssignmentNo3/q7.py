def check_name_in_string(name, input_string):
    if name.lower() in input_string.lower():
        return True
    else:
        return False

def main():
    my_name = "Aayush Raj"
    input_string = "My name is Aayush Raj. I am a programmer."

    if check_name_in_string(my_name, input_string):
        print("Your name is present in the string.")
    else:
        print("Your name is not present in the string.")

if __name__ == "__main__":
    main()
