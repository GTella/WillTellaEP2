def define_posicoes(dados_de_posicionamento):
    linha = dados_de_posicionamento["linha"]
    coluna = dados_de_posicionamento["coluna"]
    orientacao = dados_de_posicionamento["orientacao"]
    tamanho = dados_de_posicionamento["tamanho"]

    posicoes = []

    if orientacao == "vertical":
        for c in range(linha, linha + tamanho):
            posicoes.append([c, coluna])

    elif orientacao == "horizontal":
        for d in range(coluna, coluna + tamanho):
            posicoes.append([linha, d])

    return posicoes