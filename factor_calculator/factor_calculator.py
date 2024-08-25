# core function that used to calculate factors
def factor(number: int) -> list:
    """
    to calculate the factors of a number.

    Args:
        number (int): the number you want to transform.

    Returns:
        list: includes the factors of the number
    """

    res_li = list()
    for i in range(1, round((number+2)/2)):
        result = number / i

        if int(result) == result:
            res_li.append(i)

    res_li.append(number)
    return res_li


# service system
num = input("[initialization] Enter an integer: ")
if num.isdigit():
    li = factor(int(num))
    if li is not None:
        print(f"[result] <{num}>'s factors are: ", end="")
        print(*li, sep=", ")
else:
    print("[error] illegal input!")

input("Finished. Press 'Enter' to exit.")
