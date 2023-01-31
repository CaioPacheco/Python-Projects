import time


def toDecimal(number, strmode=True):

    result = 0
    number = number.lstrip('0')
    lenght = len(number)

    for x in range(lenght):

        if saida == True:
            time.sleep(0.05)

        if number[x] == '1':
            result += (2**(lenght-x-1))

        if saida == True:
            print('  |  ' + number[x] + '  |  Total: ' + str(result) +
                  '  |  Adicionado: ' + str(int(number[x])*(2**(lenght-x-1))) + '    ')

    if saida == True:
        time.sleep(0.07)

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

        if saida == True:
            time.sleep(0.05)

        localresult = number//2
        resto = number % 2
        number = number//2
        result = result + str(resto)

        if localresult == 1:

            time.sleep(0.02)
            if saida == True:
                print('  |  Quociente: ' + str(localresult) + '  |  Resto: ' +
                      str(resto) + '  |  Resultado Parcial: ' + result + '  |  End of flow')
            result = result + '1'
            break

        if saida == True:
            print('  |  Quociente: ' + str(localresult) + '  |  Resto: ' +
                  str(resto) + '  |  Resultado Parcial: ' + result + '    ')

    lenght = len(result)

    for x in range(lenght):
        invresult = invresult + result[lenght-x-1]

    print('')

    if strmode == True:
        return invresult
    else:
        return int(invresult)


def toHexadecimal(number, strmode=True):

    if int(number) <= 1:
        return '1'

    result = ''
    invresult = ''
    number = number.lstrip('0')
    number = int(number)
    dic = ['A', 'B', 'C', 'D', 'E', 'F']

    while True:

        if saida == True:
            time.sleep(0.05)

        localresult = number//16
        resto = number % 16
        number = number//16

        if resto >= 10:
            restolocal = resto - 10
            result = result + dic[restolocal]
        else:
            result = result + str(resto)

        if localresult == 16 and resto == 0:
            result = result + '0'

        if localresult <= 16:

            time.sleep(0.02)

            if saida == True:
                print('  |  Quociente: ' + str(localresult) + '  |  Resto: ' +
                      str(resto) + '  |  Resultado Parcial: ' + result + '  |  End of flow')

            if resto != 0:
                result = result + str(localresult)
            else:
                result = result + '1'

            break

        if saida == True:
            print('  |  Quociente: ' + str(localresult) + '  |  Resto: ' +
                  str(resto) + '  |  Resultado Parcial: ' + result + '    ')

    lenght = len(result)

    for x in range(lenght):
        invresult = invresult + result[lenght-x-1]

    print('')

    if strmode == True:
        return invresult
    else:
        return int(invresult)


saida = False

while True:

    if saida == True:
        print('| 1: Converter para binário | 2: Converter para decimal | 3: Converter para hexadecimal | 4: Desligar saída de dados | 5: Sair |')
    else:
        print('| 1: Converter para binário | 2: Converter para decimal | 3: Converter para hexadecimal | 4: Ligar saída de dados | 5: Sair |')

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

        if saida == True:
            saida = False
            print('Saída de dados desligada.')
        else:
            saida = True
            print('Saída de dados ligada.')

    elif entrada == '5':
        break

    else:
        print('Opção inválida')
        time.sleep(0.6)

    print('')
    if saida == True:
        time.sleep(0.6)
