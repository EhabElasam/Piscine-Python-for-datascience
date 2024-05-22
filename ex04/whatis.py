import sys

def main():
    try: 
        if len(sys.argv) == 1:
            print()
            return
        assert (len(sys.argv) == 2), "Too many arguments"
        if sys.argv[1] is not isdigit() or sys.argv[1][1:].isdigit()and sys.argv[1][0] != '-':
            assert sys.argv[1][0] == '-', "Argument is not an integer"
    except Exception as e:
        print("AssertionError: ", e)
        return

    if int(sys.argv[1]) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()
