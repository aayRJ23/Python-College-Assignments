def find_max_ascii_letter(s):
    max_ascii_letter = ''
    max_ascii_value = 0

    for char in s:
        if char.isalpha():
            ascii_value = ord(char)
            if ascii_value > max_ascii_value:
                max_ascii_value = ascii_value
                max_ascii_letter = char

    return max_ascii_letter

def main():
    s = 'The lazy fox jumps over the brown dog'

    max_ascii_letter = find_max_ascii_letter(s)
    print(f"The letter with the maximum ASCII value in the string is: {max_ascii_letter}")

if __name__ == "__main__":
    main()
