def deep_first_search(stones: List[int]): 
    if all(x == 0 for x in stones):
        # no more stones 
        return False 
    for i in range(len(stones)):
        for j in range(1, len(stones) + 1): 
            if not deep_first_search(stones[:i] + [stones[i] - j] + [stones[i + 1:]]):
                # there is a next losing scenario
                return True
    # all next scenarios are 
    return False
