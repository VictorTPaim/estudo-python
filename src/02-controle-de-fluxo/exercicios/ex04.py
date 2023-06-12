'''Implemente o ex03.py mas ao final do programa dever ser apresentado ao usuário todos os problemas 
que o identificador informado possui (implementar como list de erros)'''

codigo_identificador = input('Digite o codigo: ')

numeros = codigo_identificador[+2:-1]
erros = []

if len(codigo_identificador) != 7:
    erros.append('O código deve possuir 7 caracteres')
if codigo_identificador[0:2] != 'BR':
    erros.append('O código deve iniciar com BR (maiusculo)')
if codigo_identificador[-1] != 'X':
    erros.append('O código deve terminar com X (maiusculo)')
if int(numeros) < 1 or int(numeros) > 9999:
    erros.append('O número deve estar entre 0001 e 9999')

if erros:
    print(erros)
else: 
    print('Código Válido')