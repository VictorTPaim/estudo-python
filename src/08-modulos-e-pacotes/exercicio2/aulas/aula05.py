from uteis import retangulo

retangulo1 = retangulo.Retangulo(10.0, 5.0)
retangulo2 = retangulo.Retangulo(3.0, 14.0)

representacao_string_retangulo = 'Retangulo(7.5, 12.3)'
print(retangulo1.__repr__())

retangulo3 = eval('retangulo.Retangulo(7.5, 12.3)')
retangulo4 = eval('representacao_string_retangulo')

print(retangulo1)
print(retangulo2)
print(retangulo3)
print(retangulo4)
