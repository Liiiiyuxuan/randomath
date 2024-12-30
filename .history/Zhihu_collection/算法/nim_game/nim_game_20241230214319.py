def deep_first_search(stones: List[int]): 
    if all(x == 0 for x in stones):
        # no more stones 
        return False 
    for i in range(len(stones)):
        for j in range(1, len(stones) + 1): 
            if not deep_first_search(stones[:i] + [stones[i] - j])
