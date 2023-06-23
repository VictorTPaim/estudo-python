from uteis import pessoa_aula08 as pessoa

programador = pessoa.Programador("José", "Augusto", "123.123.123-12", 5000, 200)
print(programador.obtem_nome_completo())
print(programador.calcula_pagamento())
print(type(programador))

# funcionario = pessoa.Funcionario("José", "Augusto", "123.123.123-12", 5000)
# print(funcionario.obtem_nome_completo())
# print(funcionario.calcula_pagamento())
# print(type(funcionario))

# cliente = pessoa.Cliente("Paulo", "Muloto", "123.123.123-12")
# print(cliente.obtem_nome_completo())
# print(type(cliente))
