from meuspacotes import interface
from meuspacotes import arquivos
from meuspacotes import leia
from meuspacotes import cores
from meuspacotes import DataHora


while True:
    #Ínicio Do programa
    #Opções 1 -> Decidir o tipo de tarefa
    r1 = interface.menu(['Tarefas Diárias', 'Tarefas Temporarias', 'Sair do Programa'], f'{cores.magenta()}', f'{cores.azul()}', f'{"GERENCIADOR DE TAREFAS":^40}'f'\n{"MENU":^40}', 'stint')
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
                                    linhasarq = []
                                    for v in linhasarqtemp:
                                        vl = ''
                                        for nl, l in enumerate(v):
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
                            cont = 1
                            for linha in arqtarefas:
                                cont += 1
                            tarefa = str(input(f'{cores.magentaclaro()}Digite a tarefa a ser adicionada: {cores.retirarcor()}'))
                            arqtarefas.write(f'{cont} - {tarefa}\n')
                            arqtarefas.close()
                        #A opção 4 Retorna para o Menu anterior
                        elif r3[0] == 4:
                            break
    elif r1[0] == 2:
        print(f'{cores.vermelhoclaro()}AVISO! Está parte do programa não está pronta para uso no momento.{cores.retirarcor()}')
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
                    # Determinada lista de tarefas é aberta para administração
                    arqtarefas = arquivos.lerarquivo(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}')
                    while True:
                        # Opções 4 -> Menu de administração da lista de tarefas
                        r3 = interface.menu(['Ver Tarefas', 'Apagar Tarefa', 'Adicionar Tarefa', 'Voltar'], f'{cores.magenta()}', f'{cores.azul()}', f'{f"GERENCIAR {r1[1].upper()}":^40}'f'\n{f"{r2[1].upper()} -> {r2b[1].upper()}":^40}', 'stint')
                        # Se opção 1 for escolhida ele mostra a lista
                        if r3[0] == 1:
                            arqtarefas = arquivos.lerarquivo(f'Tarefas/{r1[1]}/{r2[1]}/{r2b[1]}')
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
                                    linhasarq = []
                                    for v in linhasarqtemp:
                                        vl = ''
                                        for nl, l in enumerate(v):
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
                            cont = 1
                            for linha in arqtarefas:
                                cont += 1
                            tarefa = str(input(f'{cores.magentaclaro()}Digite a tarefa a ser adicionada: {cores.retirarcor()}'))
                            print('<> Defina a data de término dessa tarefa <>')
                            anofimtar = str(input('Ano: '))
                            mesfimtar = str(input('Mês: '))
                            diafimtar = str(input('Dia: '))
                            horafimtar = str(input('Hora: '))
                            minfimtar = str(input('Minuto: '))
                            segunfimtar = str(input('Segundo: '))
                            arqtarefas.write(f'{cont} - {tarefa} -> Ínicio: {DataHora.VerificaData.retorna_data_hora_atual()} -> Término: {anofimtar}-{mesfimtar}-{diafimtar} {horafimtar}:{minfimtar}:{segunfimtar}\n')
                            arqtarefas.close()
                            with open(f'Tarefas/{r1[1]}/Datas/{r2[1]}/{r2b[1]}', 'w+') as arqdata:
                                arqdata.write(f'{anofimtar}-{mesfimtar}-{diafimtar} {horafimtar}:{minfimtar}:{segunfimtar}')
                        # A opção 4 Retorna para o Menu anterior
                        elif r3[0] == 4:
                            break
    elif r1[0] == 3:
        interface.linha(40)
        print(f'{cores.magentaclaro()}Até logo.{cores.retirarcor()}')
        break
