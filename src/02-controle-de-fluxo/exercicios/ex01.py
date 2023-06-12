""" Solicite ao usuário 3 notas e apresente o resultado da média aritmética das notas """

nota_01 = float(input('Digite sua primeira nota: '))
nota_02 = float(input('Digite sua segunda nota: '))
nota_03 = float(input('Digite sua terceira nota: '))

NOTA_01_VALIDA = 0 <= nota_01 <= 10
NOTA_02_VALIDA = 0 <= nota_02 <= 10
NOTA_03_VALIDA = 0 <= nota_03 <= 10

if NOTA_01_VALIDA and NOTA_02_VALIDA and NOTA_03_VALIDA:
    media = (nota_01 + nota_02 + nota_03) / 3
    print(f'Sua média é: {media}')
else:
    print('Notas inválidas.')
