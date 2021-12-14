def number_valid(chaine):
    """Number Valid :
    Determine if the text in the input is a number between 0 and 493

    Args:
        chaine (str): the input of the user

    Returns:
        [bool]: True if the input is an integer between 0 and 493 else False
    """
    try:
        if chaine == "":
            return True
        number = int(chaine)
        if number in range(0, 494):
            return True
        else:
            return False
    except ValueError:
        return False
