from functools import cache

@cache
def fibonacci(n):
    """ fibonacci
    
    This the rercusive function of the fibonacci suite
    
    Args:
        n (int): the index of fibonacci

    Returns:
        [int]: the number of fibonacci at n index
    """
    if n in [0,1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)