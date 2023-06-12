''' 
O código identificador de funcionários de uma empresa contém 7 caracteres, inicia com a sequência de caracteres BR, 
em seguida apresenta um número inteiro entre 0001 e 9999 e finaliza com o caractere X.
Crie um programa em python que solicita ao usuário um identificado e apresenta se o que foi informado é um valor válido ou inválido. 
'''

codigo_identificador = input('Digite o código identificador: ')

if len(codigo_identificador) == 7 and codigo_identificador[0:2] == 'BR' and codigo_identificador[-1] == 'X' :
    numeros = codigo_identificador[2:6]
    if 1 <= int(numeros) <= 9999:
        print('Codigo Válido')
    else:
        print('Codigo Invalido')
else:
    print('Código Inválido')