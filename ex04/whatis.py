import sys


def main():
    """
    Main function to check if the provided argument is an integer and
    determine if it is odd or even.
    """
    try:
        if len(sys.argv) == 1:
            return
        assert len(sys.argv) == 2, "Too many arguments provided"

        arg = sys.argv[1]
        if arg[0] == '-':
            assert arg[1:].isdigit(), "Argument is not an integer"
        else:
            assert arg.isdigit(), "Argument is not an integer"

        if int(arg) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")

    except AssertionError as e:
        print("AssertionError:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()
