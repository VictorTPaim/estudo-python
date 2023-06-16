''' crie a função carregar_dados_alunos que recebe como parâmetro o nome 
de um arquivo que contém dados de alunos e retorna uma tupla, onde cada 
elemento é um dicionário com as seguintes chaves: prontuario, nome e email '''

with open("src/06-arquivos/exercicios/dados_alunos.txt", "r", encoding="utf-8") as dados_alunos:

    def carregar_dados_alunos(dados_alunos):
        tupla_dicionario = ()
        for dado in dados_alunos:
            dado_tratado = dado.strip().split(sep=',')
            prontuario, nome, email = dado_tratado
            info_aluno = {
                'prontuario': prontuario,
                'nome': nome,
                'email': email
            }
            tupla_dicionario += (info_aluno,)
        return tupla_dicionario

    tupla_dados_alunos = carregar_dados_alunos(dados_alunos)
    for aluno in tupla_dados_alunos:
        print('{')
        for key, value in aluno.items():
            print(f'    {key}: {value}')
        print('}')