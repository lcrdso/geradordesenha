import random
import string
import tkinter


def numero_aleatorio():
    return str(random.randrange(10))


def letra_aleatoria():
    return random.choice(string.ascii_letters)


def simbolo_aleatorio():
    return random.choice(string.punctuation)


def escolha_tipo():
    return str(random.randrange(3))


def escolha_tipo_letra_e_numero():
    return str(random.randrange(2))


def somente_numeros():
    lista1 = []
    quantidade_caracteres = int(input('Número de caracteres da senha: '))
    for quantidade in range(quantidade_caracteres):
        lista1.append(numero_aleatorio())
    return lista1


def somente_letras():
    lista1 = []
    quantidade_caracteres = int(input('Número de caracteres da senha: '))
    for quantidade in range(quantidade_caracteres):
        lista1.append(letra_aleatoria())
    return lista1


def somente_letra_e_numeros():
    lista1 = []
    quantidade_caracteres = int(input('Número de caracteres da senha: '))
    for quantidade in range(quantidade_caracteres):
        seletor = escolha_tipo_letra_e_numero()
        if seletor == '0':
            lista1.append(letra_aleatoria())
        elif seletor == '1':
            lista1.append(numero_aleatorio())
    return lista1


def todos_os_caracteres():
    lista1 = []
    quantidade_caracteres = int(input('Número de caracteres da senha: '))
    for quantidade in range(quantidade_caracteres):
        seletor = escolha_tipo()
        if seletor == '0':
            lista1.append(letra_aleatoria())
        elif seletor == '1':
            lista1.append(simbolo_aleatorio())
        elif seletor == '2':
            lista1.append(numero_aleatorio())
    return lista1


def selecao_de_tipo(selecao):
    if selecao == 'l':
        senha_lista = somente_letras()
    elif selecao == 'n':
        senha_lista = somente_numeros()
    elif selecao == 'ln':
        senha_lista = somente_letra_e_numeros()
    elif selecao == 'lns':
        senha_lista = todos_os_caracteres()
    else:
        print('Valor invalido')
        exit()

    return senha_lista


print('Selecione a forma que a senha deve ser gerada.')

tipo_escolhido = input(
    '(l) = letras / (n) = números / (ln) = letras e números / (lns) = letras, números e simbolos: ').lower()

lista_gerada = selecao_de_tipo(tipo_escolhido)

senhagerada = ''.join(lista_gerada)

print(senhagerada)
