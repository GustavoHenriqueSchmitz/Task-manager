#Módulos utilizados
import datetime

from ferramentas import interface
from ferramentas import arquivos
from ferramentas import leia
from ferramentas import cores
from ferramentas import DataHora


#Ínicio Do programa
while True:
    #Uma escada de laços while, com as opções necessárias para o usuário chegar na lista de tarefas desejada e modificala do jetio que preferir.
    r1 = interface.menu(['Tarefas Diárias', 'Tarefas Temporárias', 'Sair do Programa'], f'{cores.magenta()}', f'{cores.azul()}', f'{"GERENCIADOR DE TAREFAS":^40}'f'\n{"MENU":^40}', 'stint')
    if r1[0] == 1:
        while True:
            r2 = interface.menu(['Tarefas Pessoais', 'Tarefas de Escola', 'Tarefas de Casa', 'Voltar ao Menu'], f'{cores.magenta()}', f'{cores.azul()}', f'{r1[1].upper().strip()}', 'stint')
            if r2[0] == 4:
                break
            while True:
                r2b = interface.menu(['Prioridade[ALTA]', 'Prioridade[MÉDIA]', 'Prioridade[BAIXA]', 'Voltar'], f'{cores.magenta()}', f'{cores.azul()}', 'DEFINIR PRIORIDADE', 'stint')
                if r2b[0] == 4:
                    break
                elif r2[0] > 0 and r2[0] < 5:
                    arqtarefas = arquivos.lerarquivo(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}')
                    while True:
                        r3 = interface.menu(['Ver Tarefas', 'Apagar Tarefa', 'Adicionar Tarefa', 'Voltar'], f'{cores.magenta()}', f'{cores.azul()}', f'{f"GERENCIAR {r1[1].upper()}":^40}'f'\n{f"{r2[1].upper()} -> {r2b[1].upper()}":^40}', 'stint')
                        #Se opção 1 for escolhida ele mostra a lista para leitura.
                        if r3[0] == 1:
                            arqtarefas = arquivos.lerarquivo(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}')
                        #A opção 2 tem como objetivo apagar uma  tarefa da lista ao escolhida
                        elif r3[0] == 2:
                            while True:
                                with open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'r') as arq:
                                    linhasarqtemp = arq.readlines() #Variavel que recebe uma lista, com as linhas do documento.
                                    if linhasarqtemp == []:
                                        print(f'{cores.vermelho()} -> Não a arquivos a serem removidos, a lista está vazia.{cores.retirarcor()}')
                                        break
                                    tarefa = leia.leiaint(f'{cores.magentaclaro()}Digite o número da tarefa a ser removida: {cores.retirarcor()}') - 1
                                    while tarefa < 0 or tarefa >= len(linhasarqtemp):
                                        print(f'{cores.vermelho()}ERRO! A tarefa digitada não existe!!!{cores.retirarcor()}')
                                        tarefa = leia.leiaint(f'{cores.magentaclaro()}Digite o número da tarefa a ser removida: {cores.retirarcor()}') - 1
                                    linhasarqtemp.remove(linhasarqtemp[tarefa])
                                    #Re-escreve a lista de tarefas porém retirando a tarefa apagada
                                    linhasarq = [] #Variavel que recebe uma lista, com as linhas do documento.
                                    for vlat in linhasarqtemp:
                                        vl = ''
                                        for nl, l in enumerate(vlat):
                                            if nl > 3:
                                                vl += f'{l}'
                                        linhasarq.append(vl)
                                    with open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'w+') as arq: #Começa a re-escrever as tarefas.
                                        for c, linha in enumerate(linhasarq):
                                            arq.write(f'{c + 1} - {linha}')
                                        break
                        #A opção 3 tem como objetivo a adição de novas tarefas ao escolhida
                        elif r3[0] == 3:
                            arqtarefas = open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'r+', encoding='utf-8')
                            contfor = 1 #Variavel responsável por organizar a numeração das tarefas. 
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
            r2 = interface.menu(['Tarefas Pessoais', 'Tarefas de Escola', 'Tarefas de Casa', 'Voltar ao Menu'],f'{cores.magenta()}', f'{cores.azul()}', f'TAREFAS {r1[1].upper().strip()}', 'stint')
            if r2[0] == 4:
                break
            while True:
                r2b = interface.menu(['Prioridade[ALTA]', 'Prioridade[MÉDIA]', 'Prioridade[BAIXA]', 'Voltar'], f'{cores.magenta()}', f'{cores.azul()}', 'DEFINIR PRIORIDADE', 'stint')
                if r2b[0] == 4:
                    break
                elif r2[0] > 0 and r2[0] < 5:
                    #Determinada lista de tarefas é aberta para administração
                    tars = open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}') #Lista de tarefas a ser verificada.
                    tarsdata = open(f'Tarefas/{r1[1]}/Datas/{r2[1]}/{r2b[1]}') #Abre o documento com as datas de término de cada tarefa da lista (tars)
                    #Variavel com a data atual. Com o ano, mês, dia, tudo dividido
                    dataatu = DataHora.RetornaData(datetime.datetime.today().strftime('%Y'), datetime.datetime.today().strftime('%m'), datetime.datetime.today().strftime('%d'), datetime.datetime.now().strftime('%H'), datetime.datetime.now().strftime('%M'), datetime.datetime.today().strftime('%S')).retorna_data_hora_sep()
                    conttar = 0 #será a variavel responsável por numerar as tarefas, ela será importante para que essa parte do código consiga localizar em qual tarefa está trabalhando.
                    #Esse dois próximos laços, são responsaveis por formatar e organizar a data de término da tarefa, para a verificação.
                    for vd in tarsdata:
                        contlist = 0
                        conttar += 1
                        vdlist = [0, 0, 0, 0, 0, 0]
                        v2 = ''
                        for c, vlat in enumerate(vd):
                            if vlat.isnumeric():
                                v2 += vlat
                            if vlat.isnumeric() == False or c + 1 == len(vd):
                                vdlist[contlist] = v2
                                contlist += 1
                                v2 = ''
                                continue
                        datai = DataHora.RetornaData(vdlist[0], vdlist[1], vdlist[2], vdlist[3], vdlist[4], vdlist[5]).retorna_data_hora_sep()
                        #Começa a verificar se as tarefas já passaram da data limite ou não.
                        for v1, v2 in zip(dataatu.values(), datai.values()):
                            #Se a data limite não tiver sido atingida, ele apenas escreve normalmente (Em Branco)
                            if int(v1) < int(v2):
                                for contlinhasm, tarm in enumerate(tars):
                                    print(f'{tarm}')
                                    break
                                break
                            #Se a data limite tiver sido atingida, ele escreve a tarefa em vermelho, indicando que a tarefa já passou de sua data de conclusão.
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
                            #Determinada lista de tarefas é aberta para administração
                            tars = open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}') #Lista de tarefas a ser verificada.
                            tarsdata = open(f'Tarefas/{r1[1]}/Datas/{r2[1]}/{r2b[1]}') #Abre o documento com as datas de término de cada tarefa da lista (tars)
                            #Variavel com a data atual. Com o ano, mês, dia, tudo dividido
                            dataatu = DataHora.RetornaData(datetime.datetime.today().strftime('%Y'), datetime.datetime.today().strftime('%m'), datetime.datetime.today().strftime('%d'), datetime.datetime.now().strftime('%H'), datetime.datetime.now().strftime('%M'), datetime.datetime.today().strftime('%S')).retorna_data_hora_sep()
                            conttar = 0 #será a variavel responsável por numerar as tarefas, ela será importante para que essa parte do código consiga localizar em qual tarefa está trabalhando.
                            #Esse dois próximos laços, são responsaveis por formatar e organizar a data de término da tarefa, para a verificação.
                            for vd in tarsdata:
                                contlist = 0
                                conttar += 1
                                vdlist = [0, 0, 0, 0, 0, 0]
                                v2 = ''
                                for c, vlat in enumerate(vd):
                                    if vlat.isnumeric():
                                        v2 += vlat
                                    if vlat.isnumeric() == False or c + 1 == len(vd):
                                        vdlist[contlist] = v2
                                        contlist += 1
                                        v2 = ''
                                        continue
                                datai = DataHora.RetornaData(vdlist[0], vdlist[1], vdlist[2], vdlist[3], vdlist[4], vdlist[5]).retorna_data_hora_sep()
                                #Começa a verificar se as tarefas já passaram da data limite ou não.
                                for v1, v2 in zip(dataatu.values(), datai.values()):
                                    #Se a data limite não tiver sido atingida, ele apenas escreve normalmente (Em Branco)
                                    if int(v1) < int(v2):
                                        for contlinhasm, tarm in enumerate(tars):
                                            print(f'{tarm}')
                                            break
                                        break
                                    #Se a data limite tiver sido atingida, ele escreve a tarefa em vermelho, indicando que a tarefa já passou de sua data de conclusão.
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
                                with open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'r') as arq: #Arquivo a ser trabalhado
                                    linhasarqtemp = arq.readlines() #Variavel na qual recebe uma lista, com cada linha da lista de tarefas.
                                    if linhasarqtemp == []:
                                        print(f'{cores.vermelho()} -> Não a arquivos a serem removidos, a lista está vazia.{cores.retirarcor()}')
                                        break
                                    tarefa = leia.leiaint(f'{cores.magentaclaro()}Digite o número da tarefa a ser removida: {cores.retirarcor()}') - 1
                                    while tarefa < 0 or tarefa >= len(linhasarqtemp):
                                        print(f'{cores.vermelho()}ERRO! A tarefa digitada não existe!!!{cores.retirarcor()}')
                                        tarefa = leia.leiaint(f'{cores.magentaclaro()}Digite o número da tarefa a ser removida: {cores.retirarcor()}') - 1
                                    linhasarqtemp.remove(linhasarqtemp[tarefa]) #Remove a tarefa indicada.
                                    arqdata = open(f'Tarefas/{r1[1]}/Datas/{r2[1]}/{r2b[1]}') #Automaticamente ele abre a lista de datas desta lista de tarefas, para apagar também a data de término desta tarefa.
                                    linhasarqdatatemp = arqdata.readlines() #Variavel na qual recebe uma lista, com cada linha da lista de datas.
                                    linhasarqdatatemp.remove(linhasarqdatatemp[tarefa]) #Remove a data de término da lista de datas.
                                    # Apartir daqui, ele re-escreve tanto a lista de tarefa, tanto a lista de datas (da lista de tarefas). Sem os valores removidos
                                    linhasarq = [] #Variavel que vai conter as linhas da lista de tarefas
                                    linhasarqdata = [] #Variavel que vai conter as linhas da lista de datas
                                    #Vai adicionando os valores nas novas listas.
                                    for vladt in linhasarqdatatemp:
                                        linhasarqdata.append(vladt)
                                    #Re-escreve o arquivo de datas
                                    with open(f'Tarefas/{r1[1]}/Datas/{r2[1]}/{r2b[1]}', 'w+') as arq:
                                        for c, linha in enumerate(linhasarqdata):
                                            arq.write(f'{linha}')
                                    for vlat in linhasarqtemp:
                                        vl = ''
                                        for nl, l in enumerate(vlat):
                                            if nl > 3:
                                                vl += f'{l}'
                                        linhasarq.append(vl)
                                    #Re-escreve a lista de tarefas
                                    with open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'w+') as arq:
                                        for c, linha in enumerate(linhasarq):
                                            arq.write(f'{c + 1} - {linha}')
                                        break
                        # A opção 3 tem como objetivo a adição de novas tarefas ao escolhida
                        elif r3[0] == 3:
                            arqtarefas = open(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}', 'r+', encoding='utf-8') #Lista de tarefas onde será adicionada a tarefa
                            contfor = 1 #Conta as linhas da lista de tarefas
                            for linha in arqtarefas:
                                contfor += 1
                            tarefa = str(input(f'{cores.magentaclaro()}Digite a tarefa a ser adicionada: {cores.retirarcor()}'))
                            print(f'{cores.magentaclaro()}<>{cores.azul()} Defina a data de término dessa tarefa {cores.magentaclaro()}<>{cores.retirarcor()}')
                            #Esta parte é responsável por definir a data limite da tarefa.
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
                                #Verifica se o ano de término já passo.
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
                                #Verifica se o valor mês existe.
                                if mesfimtar < 1 or mesfimtar > 12:
                                    print(f'{cores.vermelho()}O mês digitado não existe.{cores.retirarcor()}')
                                    print(f'{cores.vermelho()}Digite um mês valido de 1 a 12{cores.retirarcor()}')
                                    continue
                                #Verifica se o mês já passou.
                                #Para isso, verifica se o ano de término é igual ao atual e se o mês de término é menor que o atual. Se ambos derem True, é porque o mês de término já passou.
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
                                #Verifica se o dia digitado existe no mês definido. Considerando se o mês tem 29 30 ou 31 dias.
                                if diafimtar < 1 or diafimtar > int(DataHora.RetornaData.retorna_dias_mes(anofimtar, mesfimtar)):
                                    print(f'{cores.vermelho()}O dia digitado não existe.{cores.retirarcor()}')
                                    print(f'{cores.vermelho()}Digite um dia valido de 1 a {DataHora.RetornaData.retorna_dias_mes(anofimtar, mesfimtar)}{cores.retirarcor()}')
                                    continue
                                #Verifica se o dia já passou.
                                #Para isso, verifica se o mês de término é igual ao atual e se o dia de término é menor que o atual. Se ambos derem True, é porque o dia de término já passou.
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
                                #Verifica se a hora digitada existe.
                                if horafimtar < 0 or horafimtar > 23:
                                    print(f'{cores.vermelho()}A hora digitada não existe.{cores.retirarcor()}')
                                    print(f'{cores.vermelho()}Digite uma hora valida de 0 a 23.{cores.retirarcor()}')
                                    continue
                                #Verifica se a hora já passou.
                                #Para isso, verifica se o dia de término é igual ao atual e se a hora de término é menor que a atual. Se ambas derem True, é porque a hora de término já passou.
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
                                #Verifica se o minuto digitado existe
                                if minfimtar < 0 or minfimtar > 59:
                                    print(f'{cores.vermelho()}O minuto digitado não existe.{cores.retirarcor()}')
                                    print(f'{cores.vermelho()}Digite um minuto valido de 0 a 59.{cores.retirarcor()}')
                                    continue
                                #Verifica se o minuto já passou.
                                #Para isso, verifica se a hora de término é igual a atual e se o minuto de término é menor que o atual. Se ambos derem True, é porque o minuto de término já passou.
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
                                #Verifica se o segundo digitado existe
                                if segunfimtar < 0 or segunfimtar > 59:
                                    print(f'{cores.vermelho()}O segundo digitado não existe.{cores.retirarcor()}')
                                    print(f'{cores.vermelho()}Digite um segundo valido de 0 a 59.{cores.retirarcor()}')
                                    continue
                                #Verifica se o segundo já passou.
                                #Para isso, verifica se o minuto de término é igual ao atual e se o segundo de término é menor que o atual. Se ambos derem True, é porque o segundo de término já passou.
                                elif segunfimtar < int(DataHora.RetornaData().retorna_tipo_especifico(6)) and minfimtar == int(DataHora.RetornaData().retorna_tipo_especifico(5)):
                                    print(f'{cores.vermelho()}O minuto {minfimtar} já passou, digite um minuto superior ou atual.{cores.retirarcor}')
                                else:
                                    break
                            #Adiciona a tarefa
                            arqtarefas.write(f'{contfor} - {tarefa} | Ínicio: {DataHora.RetornaData().retorna_data_hora_jun()} -> Término: {anofimtar}-{mesfimtar}-{diafimtar} {horafimtar}:{minfimtar}:{segunfimtar}\n')
                            arqtarefas.close()
                            #E também já define sua data de término na lista de datas.
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
