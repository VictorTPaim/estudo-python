""" Aula 01 - Módulos e Pacotes """

# Modularização
# Focos:
# - Dividir um programa grande
# - Aumentar legibilidade
# - Facilitar manutenção

from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {numeros.dobro(num)}')
