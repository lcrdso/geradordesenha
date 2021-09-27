import random
import string


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
    for quantidade in range(quantidade_caracteres):
        lista1.append(numero_aleatorio())
    return lista1


def somente_letras():
    for quantidade in range(quantidade_caracteres):
        lista1.append(letra_aleatoria())
    return lista1


def somente_simbolos():
    for quantidade in range(quantidade_caracteres):
        lista1.append(simbolo_aleatorio())
    return lista1


def somente_letra_e_numeros():
    for quantidade in range(quantidade_caracteres):
        seletor = escolha_tipo_letra_e_numero()
        if seletor == '0':
            lista1.append(letra_aleatoria())
        elif seletor == '1':
            lista1.append(numero_aleatorio())
    return lista1


def todos_os_caracteres():
    for quantidade in range(quantidade_caracteres):
        seletor = escolha_tipo()
        if seletor == '0':
            lista1.append(letra_aleatoria())
        elif seletor == '1':
            lista1.append(simbolo_aleatorio())
        elif seletor == '2':
            lista1.append(numero_aleatorio())
    return lista1


lista1 = []
quantidade_caracteres = int(input('Número de caracteres da senha: '))
senha_lista = todos_os_caracteres()
senhagerada = ''.join(senha_lista)
print(senhagerada)