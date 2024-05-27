# import time
import sys


def ft_tqdm(lst: range) -> None:
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
