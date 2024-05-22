import sys

class ArgumentError(Exception):
    pass

# Morse-Code-Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

def main():
    if len(sys.argv) != 2:
        print("Error: Incorrect number of arguments.")
        print("Usage: python3 sos.py <string>")
        raise ArgumentError("the arguments are bad")
    
    input_string = sys.argv[1]
    
    try:
        morse_code = ' '.join(MORSE_CODE_DICT[char.upper()] for char in input_string)
        print(morse_code)
    except KeyError:
        print("Error: The input contains unsupported characters.")
        print("Usage: python3 sos.py <string>")
        raise ArgumentError("the arguments are bad")

if __name__ == "__main__":
    try:
        main()
    except ArgumentError as e:
        print(e)
        sys.exit(1)
