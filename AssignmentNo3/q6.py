def count_letters_in_names(friends):
    letter_count = {}
    for friend in friends:
        num=0
        for letter in friend:
            num+=1
        letter_count[friend]=num
    return letter_count

def main():
    # List of your ten friends' names
    friends = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank", "Grace", "Hannah", "Isaac", "Jack"]

    # Count letters in the names of your friends
    letter_count = count_letters_in_names(friends)

    # Print the letter count
    print("Letter counts in the names of your friends:")
    for friend, count in letter_count.items():
        print(f"{friend}: {count}")

if __name__ == "__main__":
    main()
