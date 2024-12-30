import time
from typing import List

def deep_first_search(stones: List[int]): 
    if all(x == 0 for x in stones):
        # no more stones 
        return False 
    for i in range(len(stones)):
        for j in range(1, stone[i] + 1): 
            if not deep_first_search(stones[:i] + [stones[i] - j] + stones[i + 1:]):
                # there is a next losing scenario
                return True
    # all next scenarios are winning
    return False

start_time = time.time()
print(deep_first_search([5, 3, 6]))
end_time = time.time()

elapsed_time = end_time - start_time 
print(f"Elapsed time: {elapsed_time:.6f} seconds.")
