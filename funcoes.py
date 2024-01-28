#CONCEITO C

def define_posicoes(posicionamento):
    linha = posicionamento["linha"]
    coluna = posicionamento["coluna"]
    orientacao = posicionamento["orientacao"]
    tamanho = posicionamento["tamanho"]

    posicoes = []

    if orientacao == "vertical":
        for c in range(linha, linha + tamanho):
            posicoes.append([c, coluna])

    elif orientacao == "horizontal":
        for d in range(coluna, coluna + tamanho):
            posicoes.append([linha, d])

    return posicoes

def preenche_frota(posicionamento, nome_navio, navios):
    tipo_navio = nome_navio
    posicoes = define_posicoes(posicionamento)

    novo_navio = {"tipo": tipo_navio, "posicoes": posicoes}
    navios.append(novo_navio)

    return navios

def faz_jogada(grid_jogo, linha, coluna):
    if grid_jogo[linha][coluna] == 1:
        grid_jogo[linha][coluna] = 'X'
    else:
        grid_jogo[linha][coluna] = '-'

    return grid_jogo

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