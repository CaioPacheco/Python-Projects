import random


def calcular_numero_verificador(digitos):

    total = 0
    numero_calculado = ['0', '0']

    for x in range(len(digitos)):
        total += int(digitos[x])*(10-x)

    vr_calc = 11-(total % 11)

    if vr_calc >= 10:
        numero_calculado[0] = str(0)
    else:
        numero_calculado[0] = str(vr_calc)

    digitos = digitos+numero_calculado[0]
    total = 0

    for x in range(len(digitos)):
        total += int(digitos[x])*(11-x)

    vr_calc = 11-(total % 11)

    if vr_calc >= 10:
        numero_calculado[1] = str(0)
    else:
        numero_calculado[1] = str(vr_calc)

    return (str(numero_calculado[0])+str(numero_calculado[1]))


def checar_cpf(cpf='000.000.000-00'):

    # Checa se a formatação está correta,
    if (len(cpf) != 14) or (cpf.count('.') != 2) or (cpf.count('-') != 1):
        # caso não estiver, retorna False.
        return False

    verify_num = ['0', '0']
    input2 = cpf
    input2 = input2.replace('.', '')
    input2 = input2.split('-')

    if len(input2[1]) != 2:
        return False

    verify_num = input2[1]

    if verify_num == (calcular_numero_verificador(input2[0])):
        result = 'Válido'
    else:
        result = 'Inválido'

    '''txt = 'Checked {} -- {}'
    print(txt.format(cpf,result))'''

    if result == 'Válido':
        return True
    elif result == 'Inválido':
        return False


def gerar_cpf(start_cpf='000.000.000'):

    if (start_cpf.count('.') != 2) or (len(start_cpf) != 11):
        start_cpf = "000.000.000"

    sec_cpf = start_cpf.split('.')
    sec1 = sec_cpf[0]
    sec2 = sec_cpf[1]
    sec3 = sec_cpf[2]

    if (len(sec1) != 3) or (len(sec2) != 3) or (len(sec3) != 3):
        sec1, sec2, sec3 = '000'

    if sec1 == '000':
        sec1 = str(random.randint(0, 999))
        if len(sec1) == 2:
            sec1 = '0'+sec1
        elif len(sec1) == 1:
            sec1 = '00'+sec1
    if sec2 == '000':
        sec2 = str(random.randint(0, 999))
        if len(sec2) == 2:
            sec2 = '0'+sec2
        elif len(sec3) == 1:
            sec2 = '00'+sec2

    if sec3 == '000':
        sec3 = str(random.randint(0, 999))
        if len(sec3) == 2:
            sec3 = '0'+sec3
        elif len(sec3) == 1:
            sec3 = '00'+sec3

    return (sec1+'.'+sec2+'.'+sec3)


while True:
    print("Para checar CPF, insira 1. Para gerar CPF, insira 2. Para sair, insira 3.")
    mode = input()
    entrada = ''

    if mode == "1":

        while True:
            print(
                'Insira CPF para checagem, no formato 000.000.000-00. Para voltar, digite "voltar".')
            entrada = input()
            if entrada.lower() == 'voltar':
                break

            match checar_cpf(entrada):
                case True:
                    print('O CPF "' + entrada + '" é válido.')
                case False:
                    print('O CPF "' + entrada + '" é inválido.')

    elif mode == "2":

        while True:
            print('Insira CPF base, no formato 000.000.000, ou pressione enter para um aleatório. Para voltar, digite "voltar".')
            entrada = input()
            if entrada.lower() == 'voltar':
                break

            saida = gerar_cpf(entrada)
            print(saida + '-' + calcular_numero_verificador(saida.replace('.', '')))

    elif mode == "3":
        break

    else:

        print("Entrada inválida.")
