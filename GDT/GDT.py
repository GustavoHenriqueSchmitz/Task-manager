#Módulos utilizados
import datetime

from meuspacotes import interface
from meuspacotes import arquivos
from meuspacotes import leia
from meuspacotes import cores
from meuspacotes import DataHora


#Ínicio Do programa
while True:
    #Opções 1 -> Decidir o tipo de tarefa
    r1 = interface.menu(['Tarefas Diárias', 'Tarefas Temporárias', 'Sair do Programa'], f'{cores.magenta()}', f'{cores.azul()}', f'{"GERENCIADOR DE TAREFAS":^40}'f'\n{"MENU":^40}', 'stint')
    if r1[0] == 1:
        while True:
            #Opção2 -> tipo de tarefa
            r2 = interface.menu(['Tarefas Pessoais', 'Tarefas de Escola', 'Tarefas de Casa', 'Voltar ao Menu'], f'{cores.magenta()}', f'{cores.azul()}', f'{r1[1].upper().strip()}', 'stint')
            if r2[0] == 4:
                break
            while True:
                #Opções 3 -> Nível de prioridade
                r2b = interface.menu(['Prioridade[ALTA]', 'Prioridade[MÉDIA]', 'Prioridade[BAIXA]', 'Voltar'], f'{cores.magenta()}', f'{cores.azul()}', 'DEFINIR PRIORIDADE', 'stint')
                if r2b[0] == 4:
                    break
                elif r2[0] > 0 and r2[0] < 5:
                    #Determinada lista de tarefas é aberta para administração
                    arqtarefas = arquivos.lerarquivo(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}')
                    while True:
                        #Opções 4 -> Menu de administração da lista de tarefas
                        r3 = interface.menu(['Ver Tarefas', 'Apagar Tarefa', 'Adicionar Tarefa', 'Voltar'], f'{cores.magenta()}', f'{cores.azul()}', f'{f"GERENCIAR {r1[1].upper()}":^40}'f'\n{f"{r2[1].upper()} -> {r2b[1].upper()}":^40}', 'stint')
                        #Se opção 1 for escolhida ele mostra a lista
                        if r3[0] == 1:
                            arqtarefas = arquivos.lerarquivo(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}')
                        #A opção 2 tem como objetivo apagar uma  tarefa da lista ao escolhida
                        elif r3[0] == 2:
                            while True:
                                with open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'r') as arq:
                                    linhasarqtemp = arq.readlines()
                                    if linhasarqtemp == []:
                                        print(f'{cores.vermelho()} -> Não a arquivos a serem removidos, a lista está vazia.{cores.retirarcor()}')
                                        break
                                    tarefa = leia.leiaint(f'{cores.magentaclaro()}Digite o número da tarefa a ser removida: {cores.retirarcor()}') - 1
                                    while tarefa < 0 or tarefa >= len(linhasarqtemp):
                                        print(f'{cores.vermelho()}ERRO! A tarefa digitada não existe!!!{cores.retirarcor()}')
                                        tarefa = leia.leiaint(f'{cores.magentaclaro()}Digite o número da tarefa a ser removida: {cores.retirarcor()}') - 1
                                    linhasarqtemp.remove(linhasarqtemp[tarefa])
                                    #Re-escreve a lista de tarefas porém retirando a tarefa apagada
                                    linhasarq = []
                                    for vlat in linhasarqtemp:
                                        vl = ''
                                        for nl, l in enumerate(vlat):
                                            if nl > 3:
                                                vl += f'{l}'
                                        linhasarq.append(vl)
                                    with open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'w+') as arq:
                                        for c, linha in enumerate(linhasarq):
                                            arq.write(f'{c + 1} - {linha}')
                                        break
                        #A opção 3 tem como objetivo a adição de novas tarefas ao escolhida
                        elif r3[0] == 3:
                            arqtarefas = open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'r+', encoding='utf-8')
                            contfor = 1
                            for linha in arqtarefas:
                                contfor += 1
                            tarefa = str(input(f'{cores.magentaclaro()}Digite a tarefa a ser adicionada: {cores.retirarcor()}'))
                            arqtarefas.write(f'{contfor} - {tarefa}\n')
                            arqtarefas.close()
                        #A opção 4 Retorna para o Menu anterior
                        elif r3[0] == 4:
                            break
    elif r1[0] == 2:
        while True:
            # Opção2 -> tipo de tarefa
            r2 = interface.menu(['Tarefas Pessoais', 'Tarefas de Escola', 'Tarefas de Casa', 'Voltar ao Menu'],f'{cores.magenta()}', f'{cores.azul()}', f'TAREFAS {r1[1].upper().strip()}', 'stint')
            if r2[0] == 4:
                break
            while True:
                # Opções 3 -> Nível de prioridade
                r2b = interface.menu(['Prioridade[ALTA]', 'Prioridade[MÉDIA]', 'Prioridade[BAIXA]', 'Voltar'], f'{cores.magenta()}', f'{cores.azul()}', 'DEFINIR PRIORIDADE', 'stint')
                if r2b[0] == 4:
                    break
                elif r2[0] > 0 and r2[0] < 5:
                    #Determinada lista de tarefas é aberta para administração
                    #E é feita a verificação se a data das tarefas já venceu ou não, se a data estiver vencida a tarefa será esrita em vermelho
                    #Ele começa preparando as variaveis
                    tars = open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}')
                    tarsdata = open(f'Tarefas/{r1[1]}/Datas/{r2[1]}/{r2b[1]}')
                    dataatu = DataHora.RetornaData(datetime.datetime.today().strftime('%Y'), datetime.datetime.today().strftime('%m'), datetime.datetime.today().strftime('%d'), datetime.datetime.now().strftime('%H'), datetime.datetime.now().strftime('%M'), datetime.datetime.today().strftime('%S')).retorna_data_hora_sep()
                    conttar = 0
                    #Começa a trabalhar no arquivo aberto na variavel tarsdata, sendo esse laço for a base de toda a verificação
                    for vd in tarsdata:
                        contlist = 0
                        conttar += 1
                        vdlist = [0, 0, 0, 0, 0, 0]
                        v2 = ''
                        #Após pegar a data no laço anterior pegamos valor por valor e vamos formatando e preparando para a verificação
                        for c, vlat in enumerate(vd):
                            if vlat.isnumeric():
                                v2 += vlat
                            if vlat.isnumeric() == False or c + 1 == len(vd):
                                vdlist[contlist] = v2
                                contlist += 1
                                v2 = ''
                                continue
                        datai = DataHora.RetornaData(vdlist[0], vdlist[1], vdlist[2], vdlist[3], vdlist[4], vdlist[5]).retorna_data_hora_sep()
                        #Começa a verificar se as tarefas já passaram da data limite ou não, escrevendo em vermelho as que já passaram
                        for v1, v2 in zip(dataatu.values(), datai.values()):
                            if int(v1) < int(v2):
                                for contlinhasm, tarm in enumerate(tars):
                                    print(f'{tarm}')
                                    break
                                break
                            if int(v1) > int(v2):
                                for contlinhasmai, tarmai in enumerate(tars):
                                    print(f'{cores.vermelho()}{tarmai}{cores.retirarcor()}')
                                    break
                                break
                            else:
                                continue
                    while True:
                        # Opções 4 -> Menu de administração da lista de tarefas
                        r3 = interface.menu(['Ver Tarefas', 'Apagar Tarefa', 'Adicionar Tarefa', 'Voltar'], f'{cores.magenta()}', f'{cores.azul()}', f'{f"GERENCIAR {r1[1].upper()}":^40}'f'\n{f"{r2[1].upper()} -> {r2b[1].upper()}":^40}', 'stint')
                        # Se opção 1 for escolhida ela mostra a lista
                        if r3[0] == 1:
                            # Determinada lista de tarefas é aberta para administração
                            # E é feita a verificação se a data das tarefas já venceu ou não, se a data estiver vencida a tarefa será esrita em vermelho
                            # Ele começa preparando as variaveis
                            tars = open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}')
                            tarsdata = open(f'Tarefas/{r1[1]}/Datas/{r2[1]}/{r2b[1]}')
                            dataatu = DataHora.RetornaData(datetime.datetime.today().strftime('%Y'),datetime.datetime.today().strftime('%m'),datetime.datetime.today().strftime('%d'),datetime.datetime.now().strftime('%H'),datetime.datetime.now().strftime('%M'),datetime.datetime.today().strftime('%S')).retorna_data_hora_sep()
                            conttar = 0
                            # Começa a trabalhar no arquivo aberto na variavel tarsdata, sendo esse laço for a base de toda a verificação
                            for vd in tarsdata:
                                contlist = 0
                                conttar += 1
                                vdlist = [0, 0, 0, 0, 0, 0]
                                v2 = ''
                                # Após pegar a data no laço anterior pegamos valor por valor e vamos formatando e preparando para a verificação
                                for c, vlat in enumerate(vd):
                                    if vlat.isnumeric():
                                        v2 += vlat
                                    if vlat.isnumeric() == False or c + 1 == len(vd):
                                        vdlist[contlist] = v2
                                        contlist += 1
                                        v2 = ''
                                        continue
                                datai = DataHora.RetornaData(vdlist[0], vdlist[1], vdlist[2], vdlist[3], vdlist[4],vdlist[5]).retorna_data_hora_sep()
                                # Começa a verificar se as tarefas já passaram da data limite ou não, escrevendo em vermelho as que já passaram
                                for v1, v2 in zip(dataatu.values(), datai.values()):
                                    if int(v1) < int(v2):
                                        for contlinhasm, tarm in enumerate(tars):
                                            print(f'{tarm}')
                                            break
                                        break
                                    if int(v1) > int(v2):
                                        for contlinhasmai, tarmai in enumerate(tars):
                                            print(f'{cores.vermelho()}{tarmai}{cores.retirarcor()}')
                                            break
                                        break
                                    else:
                                        continue
                        # A opção 2 tem como objetivo apagar uma  tarefa da lista ao escolhida
                        elif r3[0] == 2:
                            while True:
                                with open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'r') as arq:
                                    linhasarqtemp = arq.readlines()
                                    if linhasarqtemp == []:
                                        print(f'{cores.vermelho()} -> Não a arquivos a serem removidos, a lista está vazia.{cores.retirarcor()}')
                                        break
                                    tarefa = leia.leiaint(f'{cores.magentaclaro()}Digite o número da tarefa a ser removida: {cores.retirarcor()}') - 1
                                    while tarefa < 0 or tarefa >= len(linhasarqtemp):
                                        print(f'{cores.vermelho()}ERRO! A tarefa digitada não existe!!!{cores.retirarcor()}')
                                        tarefa = leia.leiaint(f'{cores.magentaclaro()}Digite o número da tarefa a ser removida: {cores.retirarcor()}') - 1
                                    linhasarqtemp.remove(linhasarqtemp[tarefa])
                                    arqdata = open(f'Tarefas/{r1[1]}/Datas/{r2[1]}/{r2b[1]}')
                                    linhasarqdatatemp = arqdata.readlines()
                                    linhasarqdatatemp.remove(linhasarqdatatemp[tarefa])
                                    linhasarq = []
                                    linhasarqdata = []
                                    for vladt in linhasarqdatatemp:
                                        linhasarqdata.append(vladt)
                                    with open(f'Tarefas/{r1[1]}/Datas/{r2[1]}/{r2b[1]}', 'w+') as arq:
                                        for c, linha in enumerate(linhasarqdata):
                                            arq.write(f'{linha}')
                                    for vlat in linhasarqtemp:
                                        vl = ''
                                        for nl, l in enumerate(vlat):
                                            if nl > 3:
                                                vl += f'{l}'
                                        linhasarq.append(vl)
                                    with open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'w+') as arq:
                                        for c, linha in enumerate(linhasarq):
                                            arq.write(f'{c + 1} - {linha}')
                                        break
                        # A opção 3 tem como objetivo a adição de novas tarefas ao escolhida
                        elif r3[0] == 3:
                            arqtarefas = open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'r+', encoding='utf-8')
                            contfor = 1
                            for linha in arqtarefas:
                                contfor += 1
                            tarefa = str(input(f'{cores.magentaclaro()}Digite a tarefa a ser adicionada: {cores.retirarcor()}'))
                            print(f'{cores.magentaclaro()}<>{cores.azul()} Defina a data de término dessa tarefa {cores.magentaclaro()}<>{cores.retirarcor()}')
                            #Esta parte é responsável por definir a data limite das tarefas.
                            #Define e verifica o ano da data limite
                            while True:
                                while True:
                                    try:
                                        anofimtar = int(input(f'{cores.magentaclaro()}Ano: {cores.retirarcor()}'))
                                    except:
                                        print(f'{cores.vermelho()} O ano digitado, é ínvalido {cores.retirarcor()}')
                                        continue
                                    else:
                                        break
                                if anofimtar < int(DataHora.RetornaData().retorna_tipo_especifico(1)):
                                    print(f'{cores.vermelho()}O ano de {anofimtar} já passou, digite um ano superior ou atual.{cores.retirarcor()}')
                                    continue
                                else:
                                    break
                            #Define e Verifica o mês da data limite
                            while True:
                                while True:
                                    try:
                                        mesfimtar = int(input(f'{cores.magentaclaro()}Mês[1/12]: {cores.retirarcor()}'))
                                    except:
                                        print(f'{cores.vermelho()}O mês digitado, é ínvalido{cores.retirarcor()}')
                                        continue
                                    else:
                                        break
                                if mesfimtar < 1 or mesfimtar > 12:
                                    print(f'{cores.vermelho()}O mês digitado não existe.{cores.retirarcor()}')
                                    print(f'{cores.vermelho()}Digite um mês valido de 1 a 12{cores.retirarcor()}')
                                    continue
                                elif mesfimtar < int(DataHora.RetornaData().retorna_tipo_especifico(2)) and anofimtar == int(DataHora.RetornaData().retorna_tipo_especifico(1)):
                                    print(f'{cores.vermelho()}O mês {mesfimtar} já passou, digite um mês superior ou atual{cores.retirarcor()}')
                                    continue
                                else:
                                    break
                            #Define e verifica o dia da data limite
                            while True:
                                while True:
                                    try:
                                        diafimtar = int(input(f'{cores.magentaclaro()}Dia: {cores.retirarcor()}'))
                                    except:
                                        print(f'{cores.vermelho()}O dia digitado, é ínvalido{cores.retirarcor()}')
                                        continue
                                    else:
                                        break
                                if diafimtar < 1 or diafimtar > int(DataHora.RetornaData.retorna_dias_mes(anofimtar, mesfimtar)):
                                    print(f'{cores.vermelho()}O dia digitado não existe.{cores.retirarcor()}')
                                    print(f'{cores.vermelho()}Digite um dia valido de 1 a {DataHora.RetornaData.retorna_dias_mes(anofimtar, mesfimtar)}{cores.retirarcor()}')
                                    continue
                                elif diafimtar < int(DataHora.RetornaData().retorna_tipo_especifico(3)) and mesfimtar == int(DataHora.RetornaData().retorna_tipo_especifico(2)):
                                    print(f'{cores.vermelho()}O dia {diafimtar} já passou, digite um dia superior ou atual.{cores.retirarcor()}')
                                else:
                                    break
                            #Define e Verifica a hora da datalimite
                            while True:
                                while True:
                                    try:
                                        horafimtar = int(input(f'{cores.magentaclaro()}Hora[0/23]: {cores.retirarcor()}'))
                                    except:
                                        print(f'{cores.vermelho()}A hora digitada, é ínvalida.{cores.retirarcor()}')
                                        continue
                                    else:
                                        break
                                if horafimtar < 0 or horafimtar > 23:
                                    print(f'{cores.vermelho()}A hora digitada não existe.{cores.retirarcor()}')
                                    print(f'{cores.vermelho()}Digite uma hora valida de 0 a 23.{cores.retirarcor()}')
                                    continue
                                elif horafimtar < int(DataHora.RetornaData().retorna_tipo_especifico(4)) and diafimtar == int(DataHora.RetornaData().retorna_tipo_especifico(3)):
                                    print(f'{cores.vermelho()}A hora {horafimtar} já passou, digite uma hora superior ou atual.{cores.retirarcor()}')
                                else:
                                    break
                            #Define e verifica o minuto da data limite
                            while True:
                                while True:
                                    try:
                                        minfimtar = int(input(f'{cores.magentaclaro()}Minuto: {cores.retirarcor()}'))
                                    except:
                                        print(f'{cores.vermelho()}O minuto digitado, é ínvalido.{cores.retirarcor()}')
                                        continue
                                    else:
                                        break
                                if minfimtar < 0 or minfimtar > 59:
                                    print(f'{cores.vermelho()}O minuto digitado não existe.{cores.retirarcor()}')
                                    print(f'{cores.vermelho()}Digite um minuto valido de 0 a 59.{cores.retirarcor()}')
                                    continue
                                elif minfimtar < int(DataHora.RetornaData().retorna_tipo_especifico(5)) and horafimtar == int(DataHora.RetornaData().retorna_tipo_especifico(4)):
                                    print(f'{cores.vermelho()}O minuto {minfimtar} já passou, digite um minuto superior ou atual.{cores.retirarcor}')
                                else:
                                    break
                            #Verifica o segundo da data limite
                            while True:
                                while True:
                                    try:
                                        segunfimtar = int(input(f'{cores.magentaclaro()}Segundo: {cores.retirarcor()}'))
                                    except:
                                        print(f'{cores.vermelho()}O segundo digitado, é ínvalido.{cores.retirarcor()}')
                                        continue
                                    else:
                                        break
                                if segunfimtar < 0 or segunfimtar > 59:
                                    print(f'{cores.vermelho()}O segundo digitado não existe.{cores.retirarcor()}')
                                    print(f'{cores.vermelho()}Digite um segundo valido de 0 a 59.{cores.retirarcor()}')
                                    continue
                                elif segunfimtar < int(DataHora.RetornaData().retorna_tipo_especifico(6)) and minfimtar == int(DataHora.RetornaData().retorna_tipo_especifico(5)):
                                    print(f'{cores.vermelho()}O minuto {minfimtar} já passou, digite um minuto superior ou atual.{cores.retirarcor}')
                                else:
                                    break
                            #Adiciona a tarefa
                            arqtarefas.write(f'{contfor} - {tarefa} | Ínicio: {DataHora.RetornaData().retorna_data_hora_jun()} -> Término: {anofimtar}-{mesfimtar}-{diafimtar} {horafimtar}:{minfimtar}:{segunfimtar}\n')
                            arqtarefas.close()
                            with open(f'Tarefas/{r1[1]}/Datas/{r2[1]}/{r2b[1]}', 'a+') as arqdata:
                                arqdata.write(f'{anofimtar}-{mesfimtar}-{diafimtar} {horafimtar}:{minfimtar}:{segunfimtar}\n')
                        # A opção 4 Retorna para o Menu anterior
                        elif r3[0] == 4:
                            break
    #Termina o programa
    elif r1[0] == 3:
        interface.linha(40)
        print(f'{cores.magentaclaro()}Até logo.{cores.retirarcor()}')
        break
