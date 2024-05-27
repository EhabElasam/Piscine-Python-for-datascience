import sys


def main():
    """
    Main function to filter words in a string
    that are longer than a given length.
    """

    # if len(sys.argv) != 2:
    #     raise AssertionError("the arguments are bad")
    if len(sys.argv) < 3:
        print("Error: Not enough arguments provided.")
        raise AssertionError("the arguments are bad")
    elif len(sys.argv) > 3:
        print("Error: Too many arguments provided.")
        raise AssertionError("the arguments are bad")

    try:
        string = sys.argv[1]
        string = sys.argv[1]
        if not string.strip():
            print("Error: The string argument must not be empty.")
            raise AssertionError("the arguments are bad")

        N = int(sys.argv[2])
    except ValueError:
        print("Error: The second argument must be an integer.")
        raise AssertionError("the arguments are bad")

    words = string.split()

    result = [word for word in words if len(word) > N]

    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)
    except Exception as e:
        print("Erorr:", e)
        sys.exit(1)
