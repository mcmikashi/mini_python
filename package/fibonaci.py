from functools import cache


@cache
def fibonacci(index):
    """ fibonacci

    This the rercusive function of the fibonacci suite

    Args:
        index (int): the index of fibonacci

    Returns:
        [int]: the number of fibonacci at n index
    """
    if index in [0, 1]:
        return index
    return fibonacci(index-1) + fibonacci(index-2)
