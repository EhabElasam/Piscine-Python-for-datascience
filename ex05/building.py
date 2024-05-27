import sys
import string


def analyze_text(text):
    """
    Analyze the text and count the occurrences of upper case letters,
    lower case letters, digits, punctuation marks, and spaces.

    Parameters:
    text (str): The text to analyze.

    Returns:
    dict: A dictionary with counts of different character types.
    """
    counts = {
        "upper_letters": sum(1 for char in text if char.isupper()),
        "lower_letters": sum(1 for char in text if char.islower()),
        "digits": sum(1 for char in text if char.isdigit()),
        "punctuation": sum(1 for char in text if char in string.punctuation),
        "spaces": sum(1 for char in text if char.isspace())
    }
    return counts


def main():
    """
    Main function to handle user input and display character counts.
    """
    try:
        if len(sys.argv) != 2:
            if len(sys.argv) == 1:
                try:
                    print("What is the text to count?")
                    file = open(0, 'r')
                    text = file.readline()
                except EOFError:
                    print("No input provided.")
                    return
            else:
                raise AssertionError("More arguments provided than required")
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

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print("\nProgram was interrupted:", e)
