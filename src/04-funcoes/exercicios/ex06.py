''' Crie um programa em python que recebe como entrada o comprimento, 
altura e a largura (cm) de um aquário e calcule as seguintes informações. '''

breakpoint()
def volume_litros(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    return (volume * 0.05) * (temperatura_desejada - temperatura_ambiente)

def filtragem_hora(volume):
    filtragem_minima1 = volume * 2
    filtragem_minima2 = volume * 3
    return f'A filtragem por hora deve estar, no mínimo, entre {filtragem_minima1} e {filtragem_minima2}'

comprimento = float(input('Digite o comprimento em cm do aquário: '))
altura = float(input('Digite a altura em cm do aquário: '))
largura = float(input('Digite a largura em cm do aquário: '))
temperatura_desejada = float(input('Digite a temperatura desejada: '))
temperatura_ambiente = float(input('Digite a temperatura ambiente: '))

volume = volume_litros(comprimento, altura, largura)
print('O volume do aquário é', volume)
potencia = potencia_termostato(volume, temperatura_desejada, temperatura_ambiente)
print('A potência ideal do termostato é:', potencia)
filtragem = filtragem_hora(volume)
print(filtragem)