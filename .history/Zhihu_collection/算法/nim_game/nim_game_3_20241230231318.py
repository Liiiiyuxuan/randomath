# See the ipynb file for more info

import time
from typing import List

def nim_game(stones: List[int]): 
    result = 0 
    for stone in stones:
        result ^= stone 
    return result

start_time = time.time()
print(nim_game([5, 3, 6]))
end_time = time.time()

elapsed_time = end_time - start_time 
print(f"Elapsed time: {elapsed_time:.6f} seconds.")

# - - - - - - - - - - dividing line - - - - - - - - - - 

start_time = time.time()
print(nim_game([5, 3, 6, 2]))
end_time = time.time()

elapsed_time = end_time - start_time 
print(f"Elapsed time: {elapsed_time:.6f} seconds.")