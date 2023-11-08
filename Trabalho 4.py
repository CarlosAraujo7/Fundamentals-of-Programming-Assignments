def inicializa():
    '''Inicializa as variáveis globais necessárias para a simulação.
    Obs: esta função é incompleta e você pode querer modificá-la'''
    
    # Pontos de diversão e de saúde
    global funpons_atuais, healthpons_atuais
    
    # Tempo atual
    global tempo_corrente
    
    # Nome e duração da última atividade feita
    global ultima_atividade, duracao_ultima_atividade
    
    global ultima_encerrada
    global cansado_de_estrelas
    # Guardando o tempo que recebi a primeira estrela
    global minuto_estrela_um
    # Qual atividade de estrela nesse momento
    global atividade_estrela_corrente
    global estrela_corrente
    
    # Pessoa está cansada
    global cansado
    
    # Valor acumulado das atividades que são feitas seguidas
    global tempo_acumulado_atividade
    
    tempo_acumulado_atividade = 0
    
    cansado = False
    
    funpons_atuais = 0
    healthpons_atuais = 0
    
    
    estrela_corrente = None
    atividade_estrela_corrente = None
    minuto_estrela_um = 0
    tempo_ultima_estrela = 0
    
    cansado_de_estrelas = False
    
    ultima_atividade = None
    duracao_ultima_atividade = 0
    
    tempo_corrente = 0
    
    ultima_encerrada = -1000
    
def estrela_pode_ser_obtida(atividade):
    global atividade_estrela_corrente, tempo_corrente, tempo_ultima_estrela, cansado_de_estrelas
        
    if (atividade_estrela_corrente == atividade and tempo_ultima_estrela == tempo_corrente):
        if (not cansado_de_estrelas):
            return True
    return False
    
def executa_atividade(atividade, duracao):
    global ultima_atividade, duracao_ultima_atividade
    global funpons_atuais, healthpons_atuais, atividade_estrela_corrente
    global tempo_corrente, cansado, tempo_acumulado_atividade
    global ultima_encerrada
    
    if (atividade == "correr"):
        
        duracao_acumulada = 180 
        
        if (ultima_atividade == "correr"):
            tempo_acumulado_atividade += duracao_ultima_atividade
            
            duracao_acumulada = 180 - tempo_acumulado_atividade
        else:
            tempo_acumulado_atividade = 0
         
        if (duracao > duracao_acumulada):
            healthpons_atuais += 3 * duracao_acumulada
            
            excede = duracao - duracao_acumulada
            
            healthpons_atuais += 1 * excede
        else:
            healthpons_atuais = healthpons_atuais + (3 * duracao)
        
        if (ultima_atividade == "correr" or ultima_atividade == "carregar" or (tempo_corrente < ultima_encerrada + 120)):
            cansado = True
        else:
            cansado = False
        
        if (not cansado_de_estrelas):
            if (atividade_estrela_corrente == "correr"):
                if (duracao > 10):
                    funpons_atuais += 3 * 10
                else:
                    funpons_atuais += 3 * duracao
        if (not cansado):
            if (duracao > 10):
               funpons_atuais += 2 * 10
               
               excede = duracao - 10
               
               funpons_atuais = funpons_atuais - (2 * excede)
            else:
                funpons_atuais += 2 * duracao
        else:
            funpons_atuais = funpons_atuais - (2 * duracao)

        tempo_corrente += duracao
        ultima_atividade = atividade
        duracao_ultima_atividade = duracao
        ultima_encerrada = tempo_corrente + duracao
        
    elif (atividade == "carregar"):
        healthpons_atuais = healthpons_atuais + (2 * duracao)
        
        if (ultima_atividade == "correr" or ultima_atividade == "carregar" or (tempo_corrente < ultima_encerrada + 120)):
            cansado = True
        else:
            cansado = False
        
        if (not cansado_de_estrelas):
            if (atividade_estrela_corrente == "carregar"):
                if (duracao > 10):
                    funpons_atuais += 3 * 10
                else:
                    funpons_atuais += 3 * duracao
            
        if (not cansado):
            if (duracao > 20):
               funpons_atuais += 1 * 20
               
               excede = duracao - 20
               
               funpons_atuais = funpons_atuais - (1 * excede)
            else:
                funpons_atuais += 1 * duracao
        else:
            funpons_atuais = funpons_atuais - (2 * duracao) 
            
        tempo_corrente += duracao
        ultima_atividade = atividade
        duracao_ultima_atividade = duracao
        ultima_encerrada = tempo_corrente + duracao
    elif (atividade == "descansar"):
        ultima_atividade = atividade
        duracao_ultima_atividade = duracao
        
        tempo_corrente += duracao
    else:
        estrela_corrente = None
        ultima_atividade = None
        duracao_ultima_atividade = 0
    
    atividade_estrela_corrente = None

def obter_funpons():
    global funpons_atuais
    return funpons_atuais
    
def obter_healthpons():
    global healthpons_atuais
    return healthpons_atuais

def oferece_estrela(atividade):
    global atividade_estrela_corrente, estrela_corrente, minuto_estrela_um
    global tempo_corrente, tempo_ultima_estrela
    
    atividade_estrela_corrente = atividade
    tempo_ultima_estrela = tempo_corrente
    
    if (estrela_corrente == None):
        estrela_corrente = "um"
        minuto_estrela_um = tempo_corrente
    elif (estrela_corrente == "um"):
        estrela_corrente = "dois"
        if (tempo_corrente > (minuto_estrela_um + 120)):
            estrela_corrente == "um"
            minuto_estrela_um = tempo_corrente
    elif (estrela_corrente == "dois"):
        if (tempo_corrente <= (minuto_estrela_um + 120)):
            cansado_de_estrelas = True
        else:
            estrela_corrente = None
        
def atividade_lucrativa_minuto():
    global ultima_atividade, atividade_estrela_corrente
    
    if (ultima_atividade == "correr" or ultima_atividade == "carregar"):
        return "descansar"
    elif (atividade_estrela_corrente == "correr"):
        return "correr"
    elif (atividade_estrela_corrente == "carregar"):
        return "carregar"
    
    elif (ultima_atividade == "descansar" or ultima_atividade == None):
        return "correr"
    
    else:
        return "carregar"
    
################################################################################
#Essas funções não são necessárias, mas recomendo implementá-las se quer função
#auxiliar.

def obter_minutos_efetivos_de_funpom(atividade):
    '''Retorna o número de minutos que o usuário obterá a quantidade máxima
       de funpons para a atividade'''
    pass
    
def obter_minutos_efetivos_de_healthpom(atividade):
    pass    

def estimar_funpom_delta(atividade, duracao):
    '''Retorna a quantiadde de funpons que um usuário obteria por executar a atividade
       por alguns minutos de duração.'''
    pass
            

def estimar_healthpom_delta(atividade, duracao):
    pass
        
################################################################################
        
if __name__ == '__main__':
    inicializa()
    executa_atividade("correr", 30)   
    print(obter_funpons())            #-20 = 10 * 2 + 20 * (-2)
    print(obter_healthpons())            #90 = 30 * 3
    print(atividade_lucrativa_minuto())  #descansar
    executa_atividade("descansar", 30)    
    oferece_estrela("correr")              
    print(atividade_lucrativa_minuto())  #correr
    executa_atividade("carregar", 30)  
    print(obter_healthpons())            #150 = 90 + 30*2
    print(obter_funpons())            #-80 = -20 + 30 * (-2)
    oferece_estrela("correr")
    executa_atividade("correr", 20)
    print(obter_healthpons())            #210 = 150 + 20 * 3
    print(obter_funpons())            #-90 = -80 + 10 * (3-2) + 10 * (-2)
    executa_atividade("correr", 170)
    print(obter_healthpons())            #700 = 210 + 160 * 3 + 10 * 1
    print(obter_funpons())            #-430 = -90 + 170 * (-2)
    
    
