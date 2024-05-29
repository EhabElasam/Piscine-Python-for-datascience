import sys


# Morse-Code-Dictionary
MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': '/'
}


def convert_to_morse(input_string):
    """
    Converts the input string to Morse code using the MORSE_CODE_DICT.

    Parameters:
    input_string (str): The string to convert to Morse code.

    Returns:
    str: The converted Morse code string.
    """

    if not all(char.isalnum() or char.isspace() for char in input_string):
        raise AssertionError("the arguments are bad")
    m_c = ' '.join(MORSE_CODE_DICT[char.upper()] for char in input_string)
    return m_c


def main():
    """
    Main function to handle command-line arguments
    and convert the input string to Morse code.
    """
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    input_string = sys.argv[1]

    morse_code = convert_to_morse(input_string)
    print(morse_code)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("AssertionError:", e)
        sys.exit(1)
