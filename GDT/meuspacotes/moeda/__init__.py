def aumentar(preco=0, taxa=0, formato=False):
    """

    :param preco: Preço
    :param taxa: Taxa% de aumento
    :param formato: Se será formatado True ou não False
    :return: Retorna o valor
    """
    res = preco + (preco * taxa / 100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return (f'{moeda}{preco:>.2f}'.replace('.', ',')) if moeda == 'R$' else (f'{moeda}{preco:>.2f}'.replace(',', '.'))


def resumo(preco=0, taxaa=1, taxar=5, formato='R$'):
    print('-' * 30)
    print('RESUMO DO VALOR'. center(30))
    print('-' * 30)
    print(f'Preço analisando: \t{moeda(preco, formato)}')
    print(f'Dobro do preço : \t{moeda(dobro(preco), formato)}')
    print(f'Metade do preço: \t{moeda(metade(preco), formato)}')
    print(f'Com {taxaa}% de aumento: {moeda(aumentar(preco, taxaa), formato)}')
    print(f'{taxar}% de redução: \t{moeda(diminuir(preco, taxar), formato)}')
    print('-' * 30)


def leiadinheiro(num):
    ndef = str(input(num)).strip()
    if ndef.replace('.', '').isnumeric() or ndef.replace(',', '').isnumeric():
        return float(ndef.replace(',', '.'))
    while True:
        print(f'\033[31mERRO: "{ndef}" é um preço inválido!\033[m')
        ndef = str(input(num)).strip()
        if ndef.replace('.', '').isnumeric() or ndef.replace(',', '').isnumeric():
            return float(ndef.replace(',', '.'))
