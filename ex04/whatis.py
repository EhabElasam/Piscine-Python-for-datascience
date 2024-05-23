import sys


def main():
    try:
        if len(sys.argv) == 1:
            return
        assert len(sys.argv) == 2, "Too much args"
        arg = sys.argv[1]
        if arg[0] == '-':
            assert arg[1:].isdigit(), "Argument is not an integer"
        else:
            assert arg.isdigit(), "Argument is not an integer"

    except Exception as e:
        print("AssertionError: ", e)
        return

    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
