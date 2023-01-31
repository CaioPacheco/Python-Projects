from typing import Union


def binary_to_decimal(binary_string: str) -> int:
    """Convert a binary string to decimal"""
    binary_string = binary_string.lstrip("0")
    decimal = 0
    for i, digit in enumerate(binary_string[::-1]):
        if digit == "1":
            decimal += 2**i
    return decimal


def decimal_to_binary(decimal: int, str_mode: bool = True) -> Union[int, str]:
    """Convert a decimal number to binary"""
    binary = bin(decimal)[2:]  # remove the "0b" prefix
    return binary if str_mode else int(binary)


def decimal_to_hexadecimal(decimal: int, str_mode: bool = True) -> Union[int, str]:
    """Convert a decimal number to hexadecimal"""
    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""
    while decimal:
        digit = decimal % 16
        hexadecimal = hex_digits[digit] + hexadecimal
        decimal = decimal // 16
    return hexadecimal if str_mode else int(hexadecimal, 16)


while True:
    print(decimal_to_binary(int(input("Entrada:"))))
