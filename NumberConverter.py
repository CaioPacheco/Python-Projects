import time
from typing import Union

def toDecimal(number, strmode=True):

    result = 0
    number = number.lstrip('0')
    lenght = len(number)

    for x in range(lenght):

        if number[x] == '1':
            result += (2**(lenght-x-1))

    print('')

    if strmode == True:
        return str(result)
    else:
        return result


def toBinary(number, strmode=True):

    if int(number) <= 1:
        return '1'

    result = ''
    invresult = ''
    number = number.lstrip('0')
    number = int(number)

    while True:

        localresult = number//2
        resto = number % 2
        number = number//2
        result = result + str(resto)

        if localresult == 1:
            result = result + '1'
            break

    invresult = result.reverse()

    print('')

    if strmode == True:
        return invresult
    else:
        return int(invresult)


def toHexadecimal(decimal: int, str_mode: bool = True) -> Union[int, str]:

    hex_digits = "0123456789ABCDEF"
    hexadecimal = ""

    while decimal:
        digit = decimal % 16
        hexadecimal = hex_digits[digit] + hexadecimal
        decimal = decimal // 16

    return hexadecimal if str_mode else int(hexadecimal, 16)


saida = False

while True:

    if saida == True:
        print('| 1: Converter para binário | 2: Converter para decimal | 3: Converter para hexadecimal | 4: Sair |')
    else:
        print('| 1: Converter para binário | 2: Converter para decimal | 3: Converter para hexadecimal | 4: Sair |')

    entrada = input()
    invalid = False

    print('')

    if entrada == '1':

        entrada2 = input(
            'Insira o número decimal a ser convertido para binário: ')

        if entrada2.isdigit():
            print('Resultado: ' + entrada2.lstrip('0') +
                  ' -> ' + toBinary(entrada2) + '  [dec -> bin]')
        else:
            print('Entrada inválida')

    elif entrada == '2':

        entrada2 = input(
            'Insira o número binário a ser convertido para decimal: ')
        invalid == False

        for x in range(len(entrada2)):
            if invalid != True:
                if entrada2[x] != '1' and entrada2[x] != '0':
                    invalid = True

        if entrada2.isdigit() and invalid == False:
            print('Resultado: ' + entrada2.lstrip('0') +
                  ' -> ' + toDecimal(entrada2) + '  [bin -> dec]')
        else:
            print('Entrada inválida')

    elif entrada == '3':

        entrada2 = input(
            'Insira o número decimal a ser convertido para hexadecimal: ')

        if entrada2.isdigit():
            print('Resultado: ' + entrada2.lstrip('0') + ' -> ' +
                  toHexadecimal(entrada2) + '  [dec -> hex]')
        else:
            print('Entrada inválida')

    elif entrada == '4':
        break

    else:
        print('Opção inválida')
        time.sleep(0.6)

    print('')
