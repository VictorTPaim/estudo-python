''' Solicite ao usuário uma única a vez as notas no formato n1, n2, n3, nm e apresente o resultado da média aritmética das notas se está aprovado (maior que 6.0), recuperação (entre 4.0 e 6.0) ou reprovado (menor que 4.0). '''

nota_dig = input('Digite suas notas no formato nota1, nota2, nota3, ...: ')
notas = [float(nota) for nota in nota_dig.split(',')]
print(notas)

soma = 0

for nota in notas:
    if nota < 0 or nota > 10:
        print('Nota inválida. A nota deve estar entre 0 e 10')
        break
    else:
        soma = soma + nota

media = soma / len(notas)
if media >= 6:
    print('Aprovado. Sua média é:', media)
elif media >= 4:
    print('Recuperação. Sua média é:', media)
else:
    print('Reprovado. Sua média é:', media)
