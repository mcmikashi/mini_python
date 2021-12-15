from functools import cache


@cache
def dying_rabbit(index: int) -> int:
    """Dying rabbit

    This the rercusive function of the dying rabbit suite

    Args:
        index (int): the index of dying rabbit

    Returns:
        [int]: the number of dying rabbit at the index
    """
    if index == "":
        return 1
    try:
        index = int(index)
        if index not in range(494):
            raise ValueError
    except ValueError as err:
        return err
    else:
        if index in range(13):
            if index in [0, 1, 2]:
                return 1
            else:
                return dying_rabbit(index-1) + dying_rabbit(index-2)
        else:
            return ((dying_rabbit(index-1) + dying_rabbit(index-2)) 
                    - dying_rabbit(index-13))


if __name__ == '__main__':
    pass
