def diferenca_segundos(tempo_1, tempo_2):
    """ (número, número) -> número

    Retorna o número de segundos a mais que um tempo em segundos
    tempo_2 tem em relação a um tempo em segundos tempo_1.
        
    >>> diferenca_segundos(1800.0, 3600.0)
    1800.0
    >>> diferenca_segundos(3600.0, 1800.0)
    -1800.0
    >>> diferenca_segundos(1800.0, 2160.0)
    360.0
    >>> diferenca_segundos(1800.0, 1800.0)
    0.0
    """

    return tempo_2 - tempo_1

def diferenca_horas(tempo_1, tempo_2):
    """ (número, número) -> float

    Retorna o número de horas a mais que um tempo em segundos
    tempo_2 tem em relação a um tempo em segundos tempo_1.
        
    >>> diferenca_horas(1800.0, 3600.0)
    0.5
    >>> diferenca_horas(3600.0, 1800.0)
    -0.5
    >>> diferenca_horas(1800.0, 2160.0)
    0.1
    >>> diferenca_horas(1800.0, 1800.0)
    0.0
    """
    
    return (tempo_2 - tempo_1) / 3600

def horas_em_float(horas, minutos, segundos):
    """ (int, int, int) -> float

    Retorna o número total de horas especificadas em horas, minutos e segundos.

    Pré-condição: 0 <= minutos < 60  e  0 <= segundos < 60

    >>> horas_em_float(0, 15, 0)
    0.25
    >>> horas_em_float(2, 45, 9)
    2.7525
    >>> horas_em_float(1, 0, 36)
    1.01
    """
    
    return horas + (minutos / 60) + (segundos / (60 * 60))

def para_horario_24_horas(horas):
    """ (número) -> número

    horas é um número de horas desde a meia noite. Retorna a hora
    como vista em um horário de 24 horas.

    Pré-condição: horas >= 0

    >>> para_horario_24_horas(24)
    0
    >>> para_horario_24_horas(48)
    0
    >>> para_horario_24_horas(25)
    1
    >>> para_horario_24_horas(4)
    4
    >>> para_horario_24_horas(28.5)
    4.5
    """

    return horas % 24

def obter_horas(horas_em_segundos):
    """ (número) -> número

    Retorna o número de segundos informados em horas.
    
    >>> obter_horas(3800)
    1
    """

    return horas_em_segundos // 3600


def obter_minutos(minutos_em_segundos):
    '''(número) -> número

    Retorna o restante dos segundos em minutos.

    >>> obter_minutos(3800)
    3
    '''
    
    return (minutos_em_segundos % 3600) // 60

def obter_segundos(segundos):
    ''' (número) -> número

    Retorna o restante dos segundos informados.

    >>> obter_segundos(3800)
    20
    '''

    return (segundos % 3600) % 60

def tempo_para_utc(diferenca_utc, tempo):
    """ (número, float) -> float

    Retorna o tempo em UTC+0, onde diferenca_utc é o número de horas distante de UTC+0.

    >>> tempo_para_utc(+0, 12.0)
    12.0
    >>> tempo_para_utc(+1, 12.0)
    11.0
    >>> tempo_para_utc(-1, 12.0)
    13.0
    >>> tempo_para_utc(-11, 18.0)
    5.0
    >>> tempo_para_utc(-1, 0.0)
    1.0
    >>> tempo_para_utc(-1, 23.0)
    0.0
    """

    return tempo - diferenca_utc

def tempo_do_utc(diferenca_utc, tempo):
    """ (número, float) -> float

    Retorna o tempo na zona com diferença diferenca_utc a partir do tempo na zona UTC.

    >>> tempo_do_utc(+0, 12.0)
    12.0
    >>> tempo_do_utc(+1, 12.0)
    13.0
    >>> tempo_do_utc(-1, 12.0)
    11.0
    >>> tempo_do_utc(+6, 6.0)
    12.0
    >>> tempo_do_utc(-7, 6.0)
    23.0
    >>> tempo_do_utc(-1, 0.0)
    23.0
    >>> tempo_do_utc(-1, 23.0)
    22.0
    >>> tempo_do_utc(+1, 23.0)
    0.0
    """

    return tempo + diferenca_utc

