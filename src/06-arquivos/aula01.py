""" Aula 01 - Manipulando arquivos """

# open("caminho", "r")

# r - Read / Leitura
# a - Append / Incrementar
# w - Write / Escrita
# x - Criar Arquivo
# r+ - Leitura + Escrita

# arquivo = open("src/06-arquivos/test3.txt", "x")

# Analisa se o arquivo pode ser lido, retornando True ou False
# print(arquivo.readable())

# Leitura do Arquivo
# arquivo = open("src/06-arquivos/test.txt", "r")
# print(arquivo.read())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline())

# lista = arquivo.readlines()
# print(lista)
# print(lista[3])

# Incrementar no arquivo
# arquivo = open("src/06-arquivos/test.txt", "a")
# arquivo.write("C\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")

# Escrever no arquivo
# arquivo = open("src/06-arquivos/test2.txt", "w")
# arquivo.write("C\n")
# arquivo.write("C++\n")
# arquivo.write("Terraform\n")

# Criar arquivo
# arquivo = open("src/06-arquivos/test3.txt", "x")
# arquivo.write("Python\n")


# arquivo.close()

# Remover arquivos
import os
# if os.path.exists("src/06-arquivos/test2.txt"):    
#     os.remove("src/06-arquivos/test2.txt")
# else:
#     print("Arquivo não existe")

# Remover pasta
os.rmdir("src/06-arquivos/nova_pasta")
