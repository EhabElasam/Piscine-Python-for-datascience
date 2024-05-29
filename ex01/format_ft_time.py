import time
from datetime import datetime


def format_ft_time():
    epoch_time = time.time()
    print(f"Seconds since January 1, 1970: {epoch_time:,.4f}"
          f" or {epoch_time:.2e} in scientific notation")
    current_date = datetime.now().strftime("%b %d %Y")
    print(current_date)


if __name__ == "__main__":
    format_ft_time()
