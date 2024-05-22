import sys

class ArgumentError(Exception):
    pass

def main():    
    if len(sys.argv) < 3:
        print("Error: Not enough arguments provided.")
        print("Usage: python3 filterstring.py <string> <integer>")
        raise ArgumentError("the arguments are bad")
    elif len(sys.argv) > 3:
        print("Error: Too many arguments provided.")
        print("Usage: python3 filterstring.py <string> <integer>")
        raise ArgumentError("the arguments are bad")
    
    try:
        string = sys.argv[1]
        string = sys.argv[1]
        if not string.strip():
            print("Error: The string argument must not be empty.")
            print("Usage: python3 filterstring.py <string> <integer>")
            raise ArgumentError("the arguments are bad")

        N = int(sys.argv[2])
    except ValueError:
        print("Error: The second argument must be an integer.")
        print("Usage: python3 filterstring.py <string> <integer>")
        raise ArgumentError("the arguments are bad")
    
    words = string.split()
    
    result = [word for word in words if len(word) > N]
    
    print(result)

if __name__ == "__main__":
    try:
        main()
    except ArgumentError as e:
        print(e)
        sys.exit(1)
