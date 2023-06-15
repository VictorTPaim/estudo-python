""" Aula 02 - Manipulando arquivos """

# arquivo = open("src/06-arquivos/arquivo.txt", "w")

# # Recebe apenas string
# # arquivo.write('olá')

# nomes = ['Caio', 'João', 'Marcos']

# # arquivo.writelines(nomes)

# for nome in nomes:
#     arquivo.write(nome + '\n')

# arquivo.close()

# with abre o arquivo mantém o ele aberto enquanto estiver dentro do contexto dele (identado)
# with open('src/06-arquivos/arquivo.txt', 'a') as arquivo:
#     # arquivo.write('\nteste append')

# with open('src/06-arquivos/arquivo.txt', 'r') as arquivo:
    # x = arquivo.read()
    # print(x, type(x))
    # x = arquivo.readlines() # Transforma em lista
    # print(x, type(x))

# with open('src/06-arquivos/arquivo.txt', 'rb') as arquivo: # Transforma em bytes
    # x = arquivo.read()
    # print(type(x.decode())) # Transforma de Bytes para String

with open('src/06-arquivos/arquivo.txt', 'r') as arquivo:
    print(next(arquivo))
    print(next(arquivo))