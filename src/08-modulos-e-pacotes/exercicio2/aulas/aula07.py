from uteis import pessoa_aula07 as pessoa
    
telefone = pessoa.Telefone('11', '1111-1111')
pessoa1 = pessoa.Pessoa('11233213', 'João da Silva', telefone, pessoa.Endereco('02233039', 123))
pessoa1.add_endereco(pessoa.Endereco('92332323', 55))

pessoa2 = pessoa.Pessoa('223232', 'Maria da Silva', telefone, pessoa.Endereco('1231221', 33))

pessoa3 = pessoa.Pessoa('3333333', 'Pedro da Silva', telefone, pessoa.Endereco('1231221', 33))

print(pessoa1)
print(pessoa1.cpf, pessoa1.nome, pessoa1.telefone)
print(pessoa1.telefone.ddd, pessoa1.telefone.numero)
print(pessoa2)

pessoa1.print_enderecos()
pessoa2.print_enderecos()
pessoa3.print_enderecos()
