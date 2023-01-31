import time

''' Define uma função para calcular os fatores primos de um determinado número '''


def fatores_primos(n):
    i = 2
    fatores = []
    ''' Usa um loop while para dividir o número de entrada pelos menores fatores primos '''
    while i * i <= n:
        ''' Verifica se o número atual é um fator primo do número de entrada '''
        if n % i:
            i += 1
        else:
            n //= i
            fatores.append(i)
            ''' Se o número de entrada não for completamente divisível por nenhum fator primo menor, 
                adicione o fator restante à lista '''
    if n > 1:
        fatores.append(n)
    return fatores


''' Use um loop while para perguntar repetidamente por novas entradas '''
while True:
    try:
        num = int(input("Insira um número: "))
        ''' Registre a hora atual antes do cálculo '''
        start_time = time.time()
        print("Os fatores primos de", num, "são:", fatores_primos(num))
        ''' Registre a hora atual depois do cálculo '''
        end_time = time.time()
        ''' Imprima o tempo gasto para calcular os fatores primos '''
        print("Tempo de processamento:", end_time - start_time, "segundos")
    except ValueError:
        ''' Se uma entrada inválida for inserida, imprima uma mensagem de erro '''
        print("Entrada inválida. Insira um número inteiro válido.")
