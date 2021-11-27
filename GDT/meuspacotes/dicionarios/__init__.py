def notas(*notas, sit=False):
    """

    :param notas: Uma ou mais notas dos alunos
    :param sit: True: Para mostra a situação/False: Para não mostrar a situação
    :return: Retorna o dicionario com varias informações da turma
    """
    turma = {}
    turma['total'] = len(notas)
    turma['maior'] = max(notas)
    turma['menor'] = min(notas)
    turma['media'] = sum(notas) / len(notas)
    if sit == True and turma['media'] >= 7:
        turma['situacao'] = 'BOA'
    elif sit == True and turma['media'] < 7:
        turma['situacao'] = 'RUIM'
    return turma