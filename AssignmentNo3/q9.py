def main():
    # Take three lines of input
    line1 = input("Enter the first line: ")
    line2 = input("Enter the second line: ")
    line3 = input("Enter the third line: ")

    # Remove spaces from each line using the replace method
    line1_no_spaces = line1.replace(" ", "")
    line2_no_spaces = line2.replace(" ", "")
    line3_no_spaces = line3.replace(" ", "")

    # Print the strings without spaces
    print("String without spaces:")
    print(line1_no_spaces)
    print(line2_no_spaces)
    print(line3_no_spaces)

if __name__ == "__main__":
    main()
