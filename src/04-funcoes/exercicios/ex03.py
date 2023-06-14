''' crie uma função que recebe uma tupla de números como parâmetro (numeros)
e retorna a soma dos números '''

def somar(numeros):
    soma = 0
    for i in numeros:
        soma = soma + i
    return soma
    
numeros_tupla = (10.0, 10.0, 10.0, 10.0, 10.0, 10.0)
print(somar(numeros_tupla))
