from functools import cache


@cache
def fibonacci(index: int) -> int:
    """ fibonacci

    This the rercusive function of the fibonacci suite

    Args:
        index (int): the index of fibonacci

    Returns:
        [int]: the number of fibonacci at the index
    """
    if index == "":
        return 0
    try:
        index = int(index)
        if index not in range(494):
            raise ValueError
    except ValueError as err:
        return err
    else:
        if index in [0, 1]:
            return index
        return fibonacci(index-1) + fibonacci(index-2)

if __name__ == '__main__':
    pass
