#CONCEITO C

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

def preenche_frota(dados_de_posicionamento, nome_navio, frota):
    tipo_embarcacao = nome_navio
    posicoes = define_posicoes(dados_de_posicionamento)

    novo_navio = {"tipo": tipo_embarcacao, "posicoes": posicoes}
    frota.append(novo_navio)

    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'

    return tabuleiro

#CONCEITO B

def posiciona_frota(navios):
    grid_jogo = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    for navio in navios:
        for pos in navio["posicoes"]:
            linha, coluna = pos
            grid_jogo[linha][coluna] = 1

    return grid_jogo

def afundados(navios, grid_jogo):
    n_afundados = 0

    for navio in navios:
        afundado = True
        for posicao in navio["posicoes"]:
            linha, coluna = posicao
        if grid_jogo[linha][coluna] != 'X':
                afundado = False
        if afundado:
            n_afundados += 1

    return n_afundados

#CONCEITO A