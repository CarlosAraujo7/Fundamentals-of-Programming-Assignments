import sys

def inicializar(nome):
    agenda = open(nome, "w")
    agenda.close()
    print("Uma agenda vazia '{}' foi criada!".format(nome))

def criar_evento(nome_banco, nome_evento, descricao, data, horario):
    agenda_leitura = open(nome_banco, "r")
    linhas = agenda_leitura.readlines()
    indices = 1

    print("Número de linhas - {}".format(len(linhas)))

    if (len(linhas) != 0):
        indices = int(linhas[len(linhas) - 1][0]) + 1

    agenda_leitura.close()
    agenda_escrita = open(nome_banco, "a")
    agenda_escrita.write(str(indices) + "," + nome_evento + "," + descricao + "," + data + "," + horario + "\n")
    agenda_escrita.close()

    print("Evento {} adicionado na agenda".format(indices))

def alterar_evento(nome_banco, indice, nome_evento, descricao, data, hora):
    agenda_leitura = open(nome_banco, "r")
    linhas = agenda_leitura.readlines()
    agenda_leitura.close()

    agenda_escrita = open(nome_banco, "w")
    auxiliar = []
    for i in range(len(linhas)):
        if linhas[i][0] == indice:
            auxiliar = linhas[i].split(",")
            if nome_evento != '':
                auxiliar[1] = nome_evento
            elif descricao != '':
                auxiliar[2] = descricao
            elif data != '':
                auxiliar[3] = data
            elif hora != '':
                auxiliar[4] = hora
            agenda_escrita.write(auxiliar[0] + "," + auxiliar[1] + "," + auxiliar[2] + "," + auxiliar[3] + "," + auxiliar[4] + "\n")
        else:
            agenda_escrita.write(linhas[i])

    agenda_escrita.close()
            
    print("Evento {} alterado na agenda".format(indice))

def remover_evento(nome_banco, indice):
    agenda_leitura = open(nome_banco, "r")
    linhas = agenda_leitura.readlines()
    agenda_leitura.close()

    agenda_escrita = open(nome_banco, "w")
    for i in range(len(linhas)):
        if linhas[i][0] != indice:   
            agenda_escrita.write(linhas[i])
    print("Evento {} removido da agenda".format(indice))

def listar_eventos(nome_banco, data):
    agenda_leitura = open(nome_banco, "r")
    linhas = agenda_leitura.readlines()
    agenda_leitura.close()
    tem_evento = False
    for i in range(len(linhas)):
        auxiliar = linhas[i].split(",")
        if auxiliar[3] == data:
            tem_evento = True
    if tem_evento == False:
        print("Não existem eventos para o dia {}".format(data))
    else:
        print("Eventos do dia {}".format(data))
        print("-----------------------------------------------")
        for i in range(len(linhas)):
            auxiliar = linhas[i].split(",")
            if auxiliar[3] == data:
                print("Evento {} - {}".format(auxiliar[0], auxiliar[1]))
                print("Descrição: {}".format(auxiliar[2]))
                print("Data: {}".format(auxiliar[3]))
                print("Hora: {}".format(auxiliar[4]))
                print("-----------------------------------------------")
           
def main(args):
    nome_banco = args[2]
    comando = args[3]

    if (comando == "inicializar"):
        inicializar(nome_banco)
    elif (comando == "criar"):
        nome_evento = args[5]
        descricao = ""
        data = ""
        hora = ""
        for i in range(len(args)):
            if (args[i] == "--nome"):
                nome_evento = args[i + 1]
            elif (args[i] == "--descricao"):
                for j in range(i + 1, len(args)):
                    if (args[j][0] != "-"):
                        descricao += args[j]
                    else:
                        break
            elif (args[i] == "--data"):
                data = args[i + 1]
            elif (args[i] == "--hora"):
                hora = args[i + 1]

        criar_evento(nome_banco, nome_evento, descricao, data, hora)

    elif (comando == "alterar"):
        nome_evento = ''
        descricao = ''
        data = ''
        hora = ''
        indice = ''

        for i in range(len(args)):
            if (args[i] == "--evento"):
                indice = args[i + 1]
            elif (args[i] == "--hora"):
                hora = args[i + 1]
            elif (args[i] == "--data"):
                data = args[i + 1]
            elif (args[i] == "--descricao"):
                descricao = args[i + 1]
            elif (args[i] == "--nome"):
                nome_evento = args[i + 1]

        alterar_evento(nome_banco, indice, nome_evento, descricao, data, hora)

    elif (comando == "remover"):
        indice = ''

        for i in range(len(args)):
            if (args[i] == "--evento"):
                indice = args[i + 1]

        remover_evento(nome_banco, indice)

    elif (comando == "listar"):
        data = ''

        for i in range(len(args)):
            if (args[i]) == ("--data"):
                data = args[i + 1]

        listar_eventos(nome_banco, data)

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
