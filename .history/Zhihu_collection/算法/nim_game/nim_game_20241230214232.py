def deep_first_search(stones: List[int]): 
    if all(x == 0 for x in stones):
        # no more stones 
        return False 
    for i in range(len(stones)):
