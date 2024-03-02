def create_mirror_string(name):
    # Reverse the name and concatenate it with the original name
    mirror_string = name + name[::-1]
    return mirror_string

def main():
    # Take the names of five friends as input
    friends = []
    for i in range(5):
        name = input(f"Enter the name of friend {i+1}: ")
        friends.append(name)

    # Convert each name into a mirror string
    mirror_strings = []
    for friend in friends:
        mirror_strings.append(create_mirror_string(friend))

    # Print the mirror strings
    print("Mirror strings:")
    for mirror_string in mirror_strings:
        print(mirror_string)

if __name__ == "__main__":
    main()
