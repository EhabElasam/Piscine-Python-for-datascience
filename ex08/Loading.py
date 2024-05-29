import sys


def ft_tqdm(lst: range) -> None:
    """
    Custom progress bar function to iterate through
    a range with progress output.

    Parameters:
    lst (range): The range to iterate over.

    Yields:
    item: The next item in the range.
    """
    total = len(lst)

    for i, item in enumerate(lst, 1):

        progress = i / total
        bar_length = 40
        block = int(round(bar_length * progress))

        bar = "#" * block + "-" * (bar_length - block)
        percent = progress * 100
        sys.stdout.write(f"\r|{bar}| {percent:.2f}% Complete | {i}/{total}")
        sys.stdout.flush()

        yield item

    print()


def main():
    """
    Main function to test the ft_tqdm function.
    """
    for item in ft_tqdm(range(100)):
        pass


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
