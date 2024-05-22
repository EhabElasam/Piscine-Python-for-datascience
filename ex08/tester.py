from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

print("ft_tqdm Progress Bar:")
for elem in ft_tqdm(range(333)):
    sleep(0.005)

print("\ntqdm Progress Bar:")
for elem in tqdm(range(333)):
    sleep(0.005)
print()
