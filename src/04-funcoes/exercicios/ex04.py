''' crie uma função que recebe vários argumentos numéricos 
através do *args retorna a soma dos números '''

def somar(*args):
    soma = 0
    for i in args:
        soma = soma + i
    return soma

print(somar(1.1, 2.2, 3.3, 4.4, 5.5))