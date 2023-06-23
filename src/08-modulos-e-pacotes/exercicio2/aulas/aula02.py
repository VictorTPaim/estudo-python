from uteis import pessoa_aula02 as pessoa

pessoa1 = pessoa.Pessoa('Maria da Silva', 'maria@email.com')
pessoa2 = pessoa.Pessoa('João Santos', 'joao@email.com')

# alterar um atributo de classe na instância (objeto)
# altera somente para aquela instância
pessoa1.especie = 'Alienigena'

# alterando um atributo de classe na classe
# altera todos os objetos e na classetambém
pessoa.Pessoa.especie = 'Alienigenas do Passado'

print(pessoa1.nome, pessoa1.email, pessoa1.especie)
print(pessoa2.nome, pessoa2.email, pessoa2.especie)

print(pessoa.Pessoa.especie)
