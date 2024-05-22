import time
import sys

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    start_time = time.time()

    for i, item in enumerate(lst, 1):
        elapsed_time = time.time() - start_time
        progress = i / total
        bar_length = 40
        block = int(round(bar_length * progress))

        bar = "#" * block + "-" * (bar_length - block)
        percent = progress * 100
        sys.stdout.write(f"\r|{bar}| {percent:.2f}% Complete | {i}/{total} | Elapsed Time: {elapsed_time:.2f}s")
        #print(f"|{bar}| {percent:.2f}% Complete | {i}/{total} | Elapsed Time: {elapsed_time:.2f}s", end='\r')
        sys.stdout.flush()

        yield item

    print()
