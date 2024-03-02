def print_kids(*kids):
    print("List of kids:")
    for kid in kids:
        print("-", kid)

def print_info(**kwargs):
    print("Student Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def main() :
    # **kids example
    print_kids("Alice", "Bob", "Charlie")
    print('');
    # **kwargs example
    print_info(name="Alice", age=12, grade="7th")

if __name__ == "__main__" :
    main()

