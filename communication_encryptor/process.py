# extention of decimal numbers
extent = dict(zip("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", range(0, 36)))


def search(num: int) -> str:
    """
    find out the character that matches the number.
    WARNING: it raises a ValueError if it is greater than 35.

    Args:
        num (int): the number you want to transform.

    Returns:
        str: the string that matches the number.
    """
    
    try:
        return list(extent.keys())[num]
    except IndexError:
        raise ValueError


def dec2other(dec_n: int, carry_over: int) -> str:
    """
    transform decimal systems to other types.

    Args:
    dec_n (int): the number you want to transform
    carry_over (int): to which base system

    Returns:
        str: other based number
    """

    res = ""
    # by taking the remainder
    # 30(from 10 base to 16 base) -> (1, 14) -> 'E1' -> '1E'
    while dec_n >= carry_over:
        dec_n, rest = divmod(dec_n, carry_over)
        res += search(rest)
    res += search(dec_n)

    return res[::-1]


def other2dec(oth_n: str, carry_over: int) -> int:
    """
    transform other base system to decimal.
    WARNING: raise a ValueError when oth_n contains illegal characters.

    Args:
        oth_n (int): the number you want to transform
        carry_over (int): define bit right

    Returns:
        int: decimal numbers
    """

    res = 0
    highest_power = len(oth_n) - 1
    # by multipying every bit with its bit right
    # '1E'(from 16 base to 10 base) -> 1*16+14 -> 30
    for char in oth_n:
        if extent[char] < carry_over:
            res += extent[char] * (carry_over ** highest_power)
        else:
            raise ValueError
        highest_power -= 1
        
    return res
