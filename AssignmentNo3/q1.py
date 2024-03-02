def print_with_index(input_string):
    for index, letter in enumerate(input_string):
        print(f"Index {index}: {letter}")

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    print_with_index(input_string)
