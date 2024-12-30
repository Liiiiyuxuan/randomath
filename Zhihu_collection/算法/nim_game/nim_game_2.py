# See the ipynb file for more info

import time
from typing import List

def hash_stones(stones: List[int]): 
    PRIME = 137 
    MOD = 1000000007
    hash_result = 0
    for stone in stones: 
        hash_result = ((hash_result * PRIME) % MOD + stone) % MOD
    return hash_result

cache = {}

def deep_first_search(stones: List[int]): 
    hash_value = hash_stones(stones)
    if hash_value in cache: 
        return cache[hash_value]
    if all(x == 0 for x in stones):
        # no more stones 
        cache[hash_value] = False
        return False 
    for i in range(len(stones)):
        for j in range(1, stones[i] + 1): 
            if not deep_first_search(stones[:i] + [stones[i] - j] + stones[i + 1:]):
                # there is a next losing scenario
                cache[hash_value] = True
                return True
    # all next scenarios are winning
    cache[hash_value] = False
    return False

start_time = time.time()
print(deep_first_search([5, 3, 6]))
end_time = time.time()

elapsed_time = end_time - start_time 
print(f"Elapsed time: {elapsed_time:.6f} seconds.")

# - - - - - - - - - - dividing line - - - - - - - - - - 

start_time = time.time()
print(deep_first_search([5, 3, 6, 2]))
end_time = time.time()

elapsed_time = end_time - start_time 
print(f"Elapsed time: {elapsed_time:.6f} seconds.")