from functools import cache


@cache
def tribonacci(index: int) -> int:
    """ tribonacci

    This the rercusive function of the tribonacci suite

    Args:
        index (int): the index of tribonacci

    Returns:
        [int]: the number of tribonacci at the index
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
            return 0
        if index == 2:
            return 1
        return tribonacci(index-1) + tribonacci(index-2) + tribonacci(index-3)

if __name__ == '__main__':
    print(tribonacci(0))
    print(tribonacci(1))
    print(tribonacci(2))
    print(tribonacci(3))