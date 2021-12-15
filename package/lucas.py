from functools import cache


@cache
def lucas(index: int) -> int:
    """ lucas

    This the rercusive function of the lucas suite

    Args:
        index (int): the index of lucas

    Returns:
        [int]: the number of lucas at the index
    """
    if index == "":
        return 2
    try:
        index = int(index)
        if index not in range(494):
            raise ValueError
    except ValueError as err:
        return err
    else:
        if index == 0:
            return 2
        if index == 1:
            return 1
        return lucas(index-1) + lucas(index-2) 

if __name__ == '__main__':
    pass
