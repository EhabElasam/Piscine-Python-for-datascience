import sys
from ft_filter import ft_filter


def main():
    """
    Main function to filter words in a string
    that are longer than a given length.
    """

    if len(sys.argv) != 3:
        raise AssertionError("the arguments are bad")

    try:
        string = sys.argv[1]
        if not string.strip():
            raise AssertionError("the arguments are bad")

        N = int(sys.argv[2])
    except ValueError:
        raise AssertionError("the arguments are bad")

    words = string.split()

    # Using a lambda function to filter words
    result = list(ft_filter(lambda word: len(word) > N, words))

    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit(1)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
