''' crie a função carregar_dados_projetos que recebe como parâmetro o nome 
de um arquivo que contém dados de projetos e retorna uma tupla, onde cada 
elemento é um dicionário com as seguintes chaves: codigo (número inteiro 
que representa o código do projeto), titulo e responsável (nome do professor 
responsável pelo projeto). '''

with open("src/06-arquivos/exercicios/dados_projetos.txt", "r", encoding="utf-8") as dados_projetos:
    def carregar_dados_projetos(dados_projetos):
        tupla_dicionario = ()
        for dado in dados_projetos:
            dado_tratado = dado.strip().split(sep=',')
            codigo, titulo, responsavel = dado_tratado
            info_projeto = {
                'codigo': int(codigo),
                'titulo': titulo,
                'responsavel': responsavel
            }
            tupla_dicionario += (info_projeto,)
        return tupla_dicionario
    
    tupla_dados_projetos = carregar_dados_projetos(dados_projetos)
    for projeto in tupla_dados_projetos:
        print('{')
        for key, value in projeto.items():
            print(f'    {key}: {value}')
        print('}')