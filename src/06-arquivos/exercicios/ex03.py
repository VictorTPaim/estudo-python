''' com base nos códigos dos exercícios anteriores, crie a função linha_para_dict 
que recebe uma linha do arquivo (string), exemplo SP000001,Maria da Silva,maria@email.com ,
uma lista com os nomes das chaves do dicionário ['prontuario', 'nome', 'email'] e retorna o 
dicionário correspondente à aquele registro. '''

with open("src/06-arquivos/exercicios/dados_arquivos.txt", "r", encoding="utf-8") as dados_arquivos:
    def carregar_dados_arquivos(dados_arquivos):
        lista = []
        for dado in dados_arquivos:
            lista.append(dado)

        valores = lista[0]
        chaves = lista[1]
        return valores, chaves
    
    def linha_para_dict(linha_arquivo, lista_chaves):
        valores = linha_arquivo.strip().split(sep=',')
        chaves = lista_chaves.strip().split(sep=',')
        dicionario = {}
        for i in range(len(chaves)):
            key = chaves[i]
            value = valores[i]
            dicionario[key] = value
        return dicionario

    valor_carregado, chave_carregada = carregar_dados_arquivos(dados_arquivos)
    dicionario = linha_para_dict(valor_carregado, chave_carregada)
    print("{")
    for chave, valor in dicionario.items():
        print(f"    '{chave}': '{valor}',")
    print("}")