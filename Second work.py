def obter_comprimento(dna):
    """ (str) -> int

    Retorna o comprimento de uma sequência de dna.

    >>> obter_comprimento('ATCGAT')
    6
    >>> obter_comprimento('ATCG')
    4
    """
    return len(dna)

def e_maior(dna1, dna2):
    """ (str, str) -> bool

    Retorna True se e somente se a sequencia dna1
    é maior que a sequencia dna2.

    >>> e_maior('ATCG', 'AT')
    True
    >>> e_maior('ATCG', 'ATCGGA')
    False
    """
    if dna1 > dna2:
        return True
    else:
        return False


def conta_nucleotideos(dna, nucleotideo):
    """ (str, str) -> int

    Retorna o número de ocorrências de um nucleotideo
    na sequencia de dna.

    >>> conta_nucleotideos('ATCGGC', 'G')
    2
    >>> conta_nucleotideos('ATCTA', 'G')
    0
    """

    ocorrencias_nucleotideo = dna.count(nucleotideo)
    return ocorrencias_nucleotideo
    
def contem_sequencia(dna1, dna2):
    """ (str, str) -> bool

    Retorna True se e somente se a sequencia de DNA dna2
    ocorre na sequencia de DNA dna1.

    >>> contem_sequencia('ATCGGC', 'GG')
    True
    >>> contem_sequencia('ATCGGC', 'GT')
    False

    """
    if dna2 in dna1:
        return True
    else:
        return False


def e_sequencia_valida(DNA):
    '''(str) -> bool

    Retorna True se e somente se a sequência de DNA for válida
    (ou seja, ela não contém caracteres diferentes de 'A', 'T', 'C' e 'G'). 

    >>>e_sequencia_valida('ATCG')
    True
    >>>e_sequencia_valida('AAAA')
    True
    >>>e_sequencia_valida('TTTT')
    True
    >>>e_sequencia_valida('CCCC')
    True
    >>>e_sequencia_valida('GGGG')
    True
    >>>e_sequencia_valida('BBBB')
    False
    >>>e_sequencia_valida('ABCD')
    False
    '''

    nucleotideo = ['A', 'T', 'C', 'G']

    for sequencia in DNA:
        if not (sequencia == 0):
            if not (sequencia in nucleotideo):
                return False
    return True

def insere_sequencia(dna1, dna2, indice):
    '''(str, str, int) -> str

    Retorna a sequência de DNA obtida inserindo a
    segunda sequência de DNA na primeira sequência de DNA no índice
    fornecido.

    >>>insere_sequencia('ATGGC','CC', 2)
    'ATCCGGC'
    >>>insere_sequencia('GGCC','AT', 3)
    'GGCATC'
    >>>insere_sequencia('CGCG', 'TA', 1)
    'CTAGCG'
    '''
    
    dna_sequencia1 = e_sequencia_valida(dna1)
    dna_sequencia2 = e_sequencia_valida(dna2)

    if dna_sequencia1 == True and dna_sequencia2 == True:
        dna = dna1 [:indice] + dna2 + dna1 [indice:] 
        return dna
    return False
   
def obter_complemento(nucleotideo):
    '''(str) -> str
    
    Um nucleotídeo é passado como parâmetro ('A', 'T', 'C' ou 'G') e retorna o
    complemento do nucleotídeo.

    >>>obter_complemento('G')
    'C'
    >>>obter_complemento('A')
    'T'
    '''
    
    dna = e_sequencia_valida(nucleotideo)
    
    if dna == True: 
        if nucleotideo == 'A':
            return 'T'
        elif nucleotideo == 'T':
            return 'A'
        elif nucleotideo == 'C':
            return  'G'
        elif nucleotideo == 'G':
            return 'C'
    return 'sem nucleotídeo.'

def obter_sequencia_complementar(dna):
    '''(str) -> str

    Retorna a sequência de DNA que é complementar à sequência de DNA fornecida.

    >>>obter_sequencia_complementar('AT')
    'TA'
    >>>obter_sequencia_complementar('ATGGCC')
    'TACCGG'
    >>>obter_sequencia_complementar('GGATCC')
    'CCTAGG'
    '''

    sequencia_complementar = ''
    i = 0
    num = len(dna)

    while i < num:
        for char in dna:
            complemento = obter_complemento(char)
            sequencia_complementar = sequencia_complementar + complemento
            i += 1
    return sequencia_complementar
