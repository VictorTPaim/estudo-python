''' Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS),
crie uma calculadora em python que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta 
em qual classificação o indivíduo se encaixa. Além disso, o programa deve apresentar a situação 
atual do indivíduo ('normal', 'perder peso', 'ganhar peso') com base na classificação Peso normal. '''

def calcular_imc(individuo):
    return individuo['peso'] / (individuo['altura'] * individuo['altura'])

def obter_classificacao(imc):
    if imc < 18.5:
        return 'Baixo peso.'
    if imc <= 24.9:
        return 'Peso Normal'
    if imc <= 29.9:
        return 'Excesso de peso'
    if imc <= 34.9:
        return 'Obesidade de classe 1'
    if imc <= 39.9:
        return 'Obesidade de classe 2'
    
    return 'Obesidade de classe 3'

def situacao_individuo(imc):
    if imc < 18.5:
        return 'Você deve ganhar peso.'
    if imc <= 24.9:
        return 'Normal'
    
    return 'Perder peso'

individuo = {
    'peso': float(input('Digite seu peso em quilos: ')),
    'altura': float(input('Digite sua altura em metros: '))
}

imc = calcular_imc(individuo)
imc_classificacao = obter_classificacao(imc)
imc_situacao = situacao_individuo(imc)
print('Seu imc é:', imc)
print('Você está classificado como:', imc_classificacao)
print('Você necessita:', imc_situacao)