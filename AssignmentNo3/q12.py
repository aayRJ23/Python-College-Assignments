def main():
    # Take five lines of input
    lines = []
    print("Enter five lines containing the word 'university' at least five times:")
    for i in range(5):
        line = input()
        lines.append(line)

    # Replace "university" with "school" in each line
    updated_lines = []
    for line in lines:
        updated_line = line.replace("university", "school")
        updated_lines.append(updated_line)

    # Print the updated lines
    print("Updated lines:")
    for updated_line in updated_lines:
        print(updated_line)

if __name__ == "__main__":
    main()


# test case
# My university offers a variety of courses.
# The university campus is located in a beautiful area.
# I graduated from the university last year.
# The university library has a vast collection of books.
# Our university hosts many events throughout the year.

