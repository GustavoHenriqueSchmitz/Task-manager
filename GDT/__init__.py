def arquivoexiste(nome):
    """

    :param nome: Nome do arquivo
    :return: Retorna True se o arquivo existir, senao retorna False
    """
    try:
        a = open(nome, 'r')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    """

    :param nome: Nome do arquivo a ser criado
    :return: Sem retorno
    """
    try:
        a = open(nome, 'wt+')
    except:
        print('\033[31mOuve um erro na criação do arquivo!\033[m')
    else:
        print('Arquivo criado com sucesso!')


def lerarquivo(nome):
    """

    :param nome: Nome do arquivo a ser lido
    :return: Sem retorno
    """
    try:
        arqui = open(nome, 'r', encoding='utf-8')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        a = arqui.read()
        print(a)
        arqui.close()