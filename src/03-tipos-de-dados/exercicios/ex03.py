meses = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}

mes_digitado = int(input('Digite o mês em formato numérico: 1, 2, 3 ... 12: '))

if mes_digitado < 1 or mes_digitado > 12:
    print('Mês inválido.')
else:
    for key, value in meses.items():
        if key == mes_digitado:
            print(value)