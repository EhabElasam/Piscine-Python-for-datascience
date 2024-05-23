import sys
import string


def analyze_text(text):
    counts = {
        "upper_letters": sum(1 for char in text if char.isupper()),
        "lower_letters": sum(1 for char in text if char.islower()),
        "digits": sum(1 for char in text if char.isdigit()),
        "punctuation": sum(1 for char in text if char in string.punctuation),
        "spaces": sum(1 for char in text if char.isspace())
    }
    return counts


def main():
    if len(sys.argv) != 2:
        if len(sys.argv) == 1:
            try:
                text = input("What is the text to count?\n")
                if text[-1] != '\n':
                    text += '\n'
            except EOFError:
                print("No input provided.")
                return
        else:
            print("AssertionError: more than one argument is provided")
            return
    else:
        text = sys.argv[1]

    counts = analyze_text(text)
    total_chars = len(text)
    print(f"The text contains {total_chars} characters:")
    print(f"{counts['upper_letters']} upper letters")
    print(f"{counts['lower_letters']} lower letters")
    print(f"{counts['punctuation']} punctuation marks")
    print(f"{counts['spaces']} spaces")
    print(f"{counts['digits']} digits")


if __name__ == "__main__":
    main()
