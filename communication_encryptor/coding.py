from process import dec2other, other2dec


def encodelongstring(ori_string: str, carry_over: int) -> str:
    """
    encode long string by unicode order.

    Args:
        ori_string (str): the original string typed by user
        carry_over (int): required by function 'dec2other'

    Returns:
        str: encoded string
    """

    res = ""
    for char in ori_string:
        order = dec2other(ord(char), carry_over)
        res += (str(order) + " ")

    return res


def decodelongstring(enc_string: str, carry_over: int) -> str:
    """
    decode long string by unicode order.

    Args:
        enc_string (str): the encrypted string typed by user
        carry_over (int): required by function 'other2dec'

    Returns:
        str: decoded string
    """
    
    res = ""
    li = enc_string.split()
    for byte in li:
        try:
            res += chr(other2dec(byte, carry_over))
        except ValueError:
            return "[error] Illegal input!"

    return res