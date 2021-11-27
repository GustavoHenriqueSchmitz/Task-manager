import meuspacotes


def linha(var=0):
    """

    :param var: Tamanho da linha ou variavel
    :return: Retorna a linha
    """
    var = str(var)
    if var.isnumeric():
        var = int(var)
        if var >= 0:
            return print('-' * var)
    else:
        lenvar = len(var) + 3
        return print('-' * lenvar)


def cabecalho(txt):
    """

    :param txt: Texto do cabeçalho
    :return: Sem retorno
    """
    print('-' * 40)
    print(txt.center(40))
    print('-' * 40)


def menu(lista, cor1='\033[m', cor2='\033[m', titulo='Menu', retorna='int'):
    """

    :param lista: Lista onde deverá ser digitado as opções do menu
    :param cor1: Primeira cor do menu
    :param cor2: Segunda Cor do menu
    :param titulo: Título do menu
    :return: Se o parâmetro retorna for int(inteiro) ele retorna o número da opção escolhida | Se o parâmetro
    for str(string) ele retorna os caracteres da opção.

    Por exemplo

    1 - Opção 1
    2 - Opção 2
    3 - opção 3

    Escolhendo int, ele reotornaria os valores 1,2,3.
    Escolhendo str, ele reotornaria os caracteres Opção 1, Opção 2, Opção 3.
    Escolhendo stint, ele reornaria tanto 1,2,3 tanto opção 1, opção 2, opção 3 os dois tipos divididos
    em uma lista.
    """
    print('-' * 40)
    print(f'{titulo:^40}')
    print('-' * 40)
    for c, item in enumerate(lista):
        print(f'{cor1}{c + 1} - {cor2}{item}\033[m')
    print('-' * 40)
    while True:
        try:
            opc = int(input(f'{cor1}Opção:\033[m '))
        except:
            print('\033[31m!!!ERRO!Digite uma opção numérica!!!\033[m')
            continue
        if opc > len(lista) or opc < 1:
            print('\033[31m!!!ERRO! Digite uma opção Valida!!!\033[m')
            continue
        else:
            if retorna.lower().strip() == 'int':
                return opc
            elif retorna.lower().strip() == 'str':
                return lista[opc - 1]
            elif retorna.lower().strip() == 'stint':
                return opc, lista[opc - 1]
