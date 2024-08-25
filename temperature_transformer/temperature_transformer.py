# core function use to change temperature
def transform(value: float, type: str) -> str:
    """
    to transform degrees between Celsius and Fahrenheit.

    Args:
        value (float): specific value of degree without marks
        type (str): explain the type is Celsius or Fahrenheit

    Returns:
        str: transformed temperature value
    """

    if type == "C":
        temp_f = value * 1.8 + 32.0
        return f"{temp_f}F"
    elif type == "F":
        temp_c = (value - 32.0) / 1.8
        return f"{temp_c}C"
    else:
        return "[error] Please enter a value that only ends up with 'c', 'C', 'f' or 'F'."


# service system
temperature = input("[content] Enter temperature value you want to transform: ")
value = temperature[0:-1]
type = temperature[-1].upper()

try:
    print(transform(float(value), type))
except ValueError:
    print("[error] Your input isn't an integer or floating point number!")
        
input("Finished. Press 'Enter' to exit.")
