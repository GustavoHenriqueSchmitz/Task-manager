import meuspacotes.interface
from random import randint, choice


def criarsenha(caracteres=0, tipo=0):
    letrasnum = ['4', 'a', 'b', '1', 'c', '0', 'd', 'e', '2', '2', 'f','3', 'g', 'h', '6', 'i', 'j', 'k', '3', 'l', 'm', '4', 'n', '5', 'o', 'p',
                 'q','6', '9', '7', 'r', 's', '8', 't', '9', '8', 'u', 'v', '7', 'w', 'x', 'y', 'z', '1', '5', '0']
    if tipo == 1:
        print('\033[35mSenha: \033[m', end='')
        for v in range(0, caracteres):
            num = randint(0, 9)
            print(f'\033[32m{num}\033[m', end='')
        print('')
    if tipo == 2:
        print('''\033[33m2.1 -\033[34m Para letras maiúsculas\033[m
\033[33m2.2 -\033[34m Para letras minúsculas\033[m''')
        tipo2 = str(input('\033[33mR:\033[m '))
        while tipo2 != '2.1' and tipo2 != '2.2':
            print(' \033[31m!> Valores digitados inválidos <!\033[m')
            tipo2 = str(input('\033[33mR:\033[m '))
        if tipo2 == '2.1':
            print('\033[35mSenha: \033[m', end='')
            for v in range(0, caracteres):
                let = choice(letrasnum)
                while let.isnumeric():
                    let = choice(letrasnum)
                print(f'\033[32m{let.upper()}\033[m', end='')
            print('')
        if tipo2 == '2.2':
            print('\033[35mSenha: \033[m', end='')
            for v in range(0, caracteres):
                let = choice(letrasnum)
                while let.isnumeric():
                    let = choice(letrasnum)
                print(f'\033[32m{let}\033[m', end='')
            print('')
    if tipo == 3:
        print('''\033[33m2.1 -\033[34m Para letras maiúsculas\033[m
\033[33m2.2 -\033[34m Para letras minúsculas\033[m''')
        tipo2 = str(input('\033[33mR:\033[m '))
        while tipo2 != '2.1' and tipo2 != '2.2':
            print(' \033[31m!> Valores digitados inválidos <!\033[m')
            tipo2 = str(input('\033[33mR:\033[m '))
        print('\033[35mSenha: \033[m', end='')
        if tipo2 == '2.1':
            for v in range(0, caracteres):
                nl = choice(letrasnum)
                print(f'\033[32m{nl.upper() if nl.isalpha() else nl}\033[m', end='')
            print('')
        if tipo2 == '2.2':
            print('\033[35mSenha: \033[m', end='')
            for v in range(0, caracteres):
                nl = choice(letrasnum)
                print(f'\033[32m{nl}\033[m', end='')
            print('')
