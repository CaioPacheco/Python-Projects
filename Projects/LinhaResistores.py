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
        
    
    if grandeza == -3:
        grandeza = 'Rosa'
    elif grandeza == -2:
        grandeza = 'Prata'
    elif grandeza == -1:
        grandeza = 'Dourada'
    elif grandeza == 0:
        grandeza = 'Preta'
    elif grandeza == 1:
        grandeza = 'Marrom'
    elif grandeza == 2:
        grandeza = 'Vermelha'
    elif grandeza == 3:
        grandeza = 'Laranja'
    elif grandeza == 4:
        grandeza = 'Amarela'
    elif grandeza == 5:
        grandeza = 'Verde'
    elif grandeza == 6:
        grandeza = 'Azul'
    elif grandeza == 7:
        grandeza = 'Violeta'
    elif grandeza == 8:
        grandeza = 'Cinza'
    elif grandeza == 9:
        grandeza = 'Branca'
            
    if tolerancia == '20':
        tolerancia = 'Nenhuma'
    elif tolerancia ==  '10':
        tolerancia = 'Prata'
    elif tolerancia ==  '5':
        tolerancia = 'Dourada'
    elif tolerancia ==  '1':
        tolerancia = 'Marrom'
    elif tolerancia ==  '2':
        tolerancia = 'Vermelha'
    elif tolerancia ==  '0.05':
        tolerancia = 'Laranja'
    elif tolerancia ==  '0.02':
        tolerancia = 'Amarela'
    elif tolerancia ==  '0.5':
        tolerancia = 'Verde'
    elif tolerancia ==  '0.25':
        tolerancia = 'Azul'
    elif tolerancia ==  '0.1':
        tolerancia = 'Violeta'
    elif tolerancia ==  '0.01':
        tolerancia = 'Cinza'
            
    resposta = algarismos
    resposta.append(grandeza)
    resposta.append(tolerancia)
    
    return resposta
        
    
    #print(resposta)
    '''print(algarismos)
    print(grandeza)
    print(tolerancia)'''
    
    
#IEC60062('1- 10')