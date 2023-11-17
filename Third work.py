"""Um tabuleiro é uma lista de listas de str. 
   Por exemplo, o tabuleiro

    ANTT
    XSOB

   é representado pela lista
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

   Uma lista de palavras é uma lista de str. 
   Por exemplo, a lista de palavras
    ANT
    BOX
    SOB
    TO
   é representada como a lista
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def e_palavra_valida(lista_palavras, palavra):
    """ (lista de str, str) -> bool

    Retorna True se e somente se palavra é um elemento de lista_palavras.

    >>> e_palavra_valida(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> e_palavra_valida(['ANT', 'BOX', 'SOB', 'TO'], 'AB')
    False
    """
    if palavra in lista_palavras:
        return True
    else:
        return False


def constroi_str_da_linha(tabuleiro, indice_linha):
    """ (lista de listas de str, int) -> str

    Retorna os caracteres da linha, com índice indice_linha do tabuleiro, 
    como uma string.

    >>> constroi_str_da_linha([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> constroi_str_da_linha([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'XSOB'
    """
    letras = ''
    for char in tabuleiro[indice_linha]:
        letras += char
    return letras
                      
def constroi_str_da_coluna(tabuleiro, indice_coluna):
    """ (lista de listas de str, int) -> str

    Returna os caracteres da coluna do tabuleiro com índice indice_coluna
    como uma única string.

    >>> constroi_str_da_coluna([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> constroi_str_da_coluna([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'AX'
    >>> constroi_str_da_coluna([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 2)
    'TO'
    """
    letras = ''
    for char in tabuleiro:
        letras += char[indice_coluna]
    return letras

def tabuleiro_contem_palavra_em_linha(tabuleiro, palavra):
    """ (lista de listas de str, str) -> bool

    Retorna True se e somente se um ou mais linha do tabuleiro contém palavra.

    Pré-condição: tabuleiro tem ao menos uma linha e coluna, e palavra é válida.

    >>> tabuleiro_contem_palavra_em_linha([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    >>> tabuleiro_contem_palavra_em_linha([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'FFF')
    False
    """
    for indice_linha in range(len(tabuleiro)):
        if palavra in constroi_str_da_linha(tabuleiro, indice_linha):
            return True

    return False


def tabuleiro_contem_palavra_em_coluna(tabuleiro, palavra):
    """ (lista de listas de str, str) -> bool

    Retorna True se e somente se uma ou mais colunas do tabuleiro contém palavra.

    Pré-condição: tabuleiro tem ao menos uma linha e coluna, e palavra é válida.


    >>> tabuleiro_contem_palavra_em_coluna([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'N')
    False
    >>> tabuleiro_contem_palavra_em_coluna([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'A')
    True
    """
    for indice_coluna in range(len(tabuleiro[0])):
        if palavra in constroi_str_da_coluna(tabuleiro, indice_coluna):
            return True
        else:
            return False
    

def tabuleiro_contem_palavra(tabuleiro, palavra):
    """ (lista de listas de str, str) -> bool

    Retorna True se e somente se palavra aparece no tabuleiro.

    Pré-condição: tabuleiro tem ao menos uma linha e coluna.

    >>> tabuleiro_contem_palavra([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>> tabuleiro_contem_palavra([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'BOLA')
    False
    """
    if tabuleiro_contem_palavra_em_coluna(tabuleiro, palavra) == True:
            return True
    elif tabuleiro_contem_palavra_em_linha(tabuleiro, palavra) == True:
            return True
    return False

def valor_palavra(palavra):
    """ (str) -> int

    Retorna os pontos obtidos ao encontrar a palavra.

    comprimento da palavra: < 3: 0 pontos
                            3-6: 1 ponto por caractere, para todos caracteres na palavra
                            7-9: 2 pontos por caractere, para todos caracteres na palavra
                            10+: 3 pontos por caractere, para todos caracteres na palavra

    >>> valor_palavra('DRUDGERY')
    16
    >>> valor_palavra('DUSTIN')
    6
    >>> valor_palavra('DOPELGANGER')
    33
    """
    p = 0
    if len(palavra) < 3:
        for pontos in range(len(palavra)):
            p = 0
            
    elif len(palavra) > 3 and len(palavra) <= 6:
        for pontos in range(len(palavra)):
            p += 1
    elif len(palavra) > 6 and len(palavra) <= 9:
        for pontos in range(len(palavra)):
            p += 2
    elif len(palavra) >= 10:
        for pontos in range(len(palavra)):
            p += 3
    return p
    

def atualiza_pontuacao(info_jogador, palavra):
    """ ([str, int] list, str) -> NoneType

    info_jogador é uma lista com nome e pontuação do jogador. Atualiza info_jogador adicionando
    o valor de pontuação da palavra à pontuação do jogador.

    >>> atualiza_pontuacao(['Jonathan', 4], 'ANT')
    ['Jonathan', 4]
    >>> atualiza_pontuacao(['Jonathan', 4], 'DUSTIN')
    ['Jonathan', 10]
    >>> atualiza_pontuacao(['Jonathan', 4], 'DOPENGANGER')
    ['Jonathan', 37]
    """
    pontuacao = info_jogador[1] + valor_palavra(palavra)
    info_jogador[1] = pontuacao

    return info_jogador

def num_palavras_no_tabuleiro(tabuleiro, palavras):
    """ (lista de listas de str, list of str) -> int

    Retorna quantas palavras aparecem no tabuleiro.

    >>> num_palavras_no_tabuleiro([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    >>> num_palavras_no_tabuleiro([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'XOB', 'SOL', 'TOB'])
    1
    >>> num_palavras_no_tabuleiro([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'SOB', 'ANTT', 'XSOB'])
    """
    palavras_tab = 0
    for indice_linha in range(len(tabuleiro)):
        for p in palavras:
            if p in constroi_str_da_linha(tabuleiro, indice_linha):
                palavras_tab += 1
            
    for indice_coluna in range(len(tabuleiro[0])):
        for p in palavras:
            if p in constroi_str_da_coluna(tabuleiro, indice_coluna):
                palavras_tab += 1

    return palavras_tab

def ler_palavras(arquivo_palavras):
    """ (arquivo aberto para leitura) -> listas de str

    Retorna a lista de todas as palavras (com newlines removidos) do arquivo aberto
    arquivo_palavras.

    Pré-condição: Cada linha do arquivo contém uma palavra em caracteres maiúsculos
    do alfabeto.
    """
    arquivo = open(arquivo_palavras,'r')
    lista = lista.readlines()
    for nome in range(len(lista)):
        lista[nome] = lista[nome].rstrip('\r\n')
    return lista

def ler_tabuleiro(arquivo_tabuleiro):
    """ (arquivo aberto para leitura) -> lista de listas de str

    Retorna um tabuleiro lido do arquivo aberto para leitura arquivo_tabuleiro. O arquivo tabuleiro conterá
    uma linha do tabuleiro por linha do arquivo. Newlines não são incluídas no tabuleiro.
    """
    arquivo_tabuleiro = open(arquivo_tabuleiro,'r')
    arquivo = arquivo_tabuleiro.readlines()
    tab = [[] for _ in range(len(arquivo) - 1)]

    for linha in range(len(arquivo) - 1):
        arquivo[linha] = arquivo[linha].replace('\n','')
        for i in range(len(arquivo[linha]) - 1):
            tab[linha].append(arquivo[linha][i])
    return tab

ler_palavras('C:/Users/Vinício/Documentos/tabuleiro1.txt')
