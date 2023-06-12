meses = (
    'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
    'Julho', 'Agosto',' Setembro', 'Outubro', 'Novembro', 'Dezembro'
)

mes_digitado = int(input('Digite o mês em formato numérico: 1, 2, 3 ... 12: '))

if mes_digitado < 1 or mes_digitado > 12:
    print("Mês inválido")
else:
    nome_mes = meses[mes_digitado - 1]
    print(nome_mes)