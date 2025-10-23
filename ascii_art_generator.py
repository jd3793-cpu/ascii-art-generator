# Simple ASCII Art Generator for letters A-Z using '#' blocks

# Define ASCII art patterns for each letter (A-Z)
ascii_letters = {
    'A': [
        "  ##  ",
        " #  # ",
        " #### ",
        " #  # ",
        " #  # "
    ],
    'B': [
        " ###  ",
        " #  # ",
        " ###  ",
        " #  # ",
        " ###  "
    ],
    'C': [
        "  ### ",
        " #    ",
        " #    ",
        " #    ",
        "  ### "
    ],
    # ... add more letters as needed
    'H': [
        " #  # ",
        " #  # ",
        " #### ",
        " #  # ",
        " #  # "
    ],
    'E': [
        " #### ",
        " #    ",
        " ###  ",
        " #    ",
        " #### "
    ],
    'L': [
        " #    ",
        " #    ",
        " #    ",
        " #    ",
        " #### "
    ],
    'O': [
        "  ##  ",
        " #  # ",
        " #  # ",
        " #  # ",
        "  ##  "
    ]
}

def print_ascii_art(text):
    text = text.upper()
    lines = [""] * 5  # 5 lines tall

    for char in text:
        if char == " ":
            # Add space between words
            for i in range(5):
                lines[i] += "   "
        elif char in ascii_letters:
            pattern = ascii_letters[char]
            for i in range(5):
                lines[i] += pattern[i] + "  "
        else:
            # For unknown chars, add question marks
            for i in range(5):
                lines[i] += "?????  "

    # Print each line
    for line in lines:
        print(line)

def main():
    print("Welcome to the ASCII Art Generator!")
    user_text = input("Enter text (A-Z only): ")
    print()
    print_ascii_art(user_text)

if __name__ == "__main__":
    main()

