def IEC60062(resistencia):
    grandeza = ''
    list_ = resistencia.split(' ')
    tolerancia = list_[1]
    pos = 0
    valor = ''
    algarismos = []
    dict_alg = {
        0 : 'Preta',
        1 : 'Marrom',
        2 : 'Vermelha',
        3 : 'Laranja',
        4 : 'Amarela',
        5 : 'Verde',
        6 : 'Azul',
        7 : 'Violeta',
        8 : 'Cinza',
        9 : 'Branca'
        }
    
    dic_grandeza = {
        -3 : 'Rosa',
        -2 : 'Prata',
        -1 : 'Dourada',
        0 : 'Preta',
        1 : 'Marrom',
        2 : 'Vermelha',
        3 : 'Laranja',
        4 : 'Amarela',
        5 : 'Verde',
        6 : 'Azul',
        7 : 'Violeta',
        8 : 'Cinza',
        9 : 'Branca'
        }

    dic_tolerancia = {
        '20' : 'Nenhuma',
        '10' : 'Prata',
        '5' : 'Dourada',
        '1' : 'Marrom',
        '2' : 'Vermelha',
        '0.05' : 'Laranja',
        '0.02' : 'Amarela',
        '0.5' : 'Verde',
        '0.25' : 'Azul',
        '0.1' : 'Violeta',
        '0.01' : 'Cinza'
        }
    
    if list_[0].find('m') >= 0:
        grandeza = -3
        pos = list_[0].find('m')
        
    elif list_[0].find('-') >= 0:
        grandeza = 0
        pos = list_[0].find('-')
        
    elif list_[0].find('K') >= 0:
        grandeza = 3
        pos = list_[0].find('K')
        
    elif list_[0].find('M') >= 0:
        grandeza = 6
        pos = list_[0].find('M')
        
    elif list_[0].find('G') >= 0:
        grandeza = 9
        pos = list_[0].find('G')
        
    valor = list_[0][:pos]
        
    
    if valor.isalnum() == False:
        valor = valor.split('.')
        quant = len(valor[1])
        grandeza -= quant
        valor = valor[0]+valor[1]
        
    if len(valor) == 1:
        algarismos.append(int(valor))
        algarismos.append(0)
        grandeza = grandeza - 1
        
    else:
        for x in range(len(valor)):
            algarismos.append(int(valor[x]))
        
    for x in range(len(algarismos)):
        algarismos[x] = dict_alg[algarismos[x]]
        
    
    grandeza = dic_grandeza[grandeza]
    tolerancia = dic_tolerancia[tolerancia]
            
    resposta = algarismos
    resposta.append(grandeza)
    resposta.append(tolerancia)
    
    return resposta
        
    
    #print(resposta)
    '''print(algarismos)
    print(grandeza)
    print(tolerancia)'''
    
    
#IEC60062('1- 10')