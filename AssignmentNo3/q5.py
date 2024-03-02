def print_name_in_format(name):
    formatted_name = f"@@@{name}@@@"
    print(formatted_name)

def main():
    name = input("Enter your name: ")
    print_name_in_format(name)

if __name__ == "__main__":
    main()
