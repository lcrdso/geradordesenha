import random
import string
import tkinter


class Gerador_senha:
    def __init__(self):
        print('Selecione a forma que a senha deve ser gerada.')

        self.tipo_escolhido = input(
            '(l) = letras / (n) = números / (ln) = letras e números / (lns) = letras, números e simbolos: ').lower()

        self.lista_gerada = self.selecao_de_tipo(self.tipo_escolhido)

        self.senhagerada = ''.join(self.lista_gerada)

        print(self.senhagerada)

    def numero_aleatorio(self):
            return str(random.randrange(10))

    def letra_aleatoria(self):
            return random.choice(string.ascii_letters)

    def simbolo_aleatorio(self):
            return random.choice(string.punctuation)

    def escolha_tipo(self):
            return str(random.randrange(3))

    def escolha_tipo_letra_e_numero(self):
            return str(random.randrange(2))

    def somente_numeros(self):
            lista1 = []
            quantidade_caracteres = int(input('Número de caracteres da senha: '))
            for quantidade in range(quantidade_caracteres):
                lista1.append(self.numero_aleatorio())
            return lista1

    def somente_letras(self):
            lista1 = []
            quantidade_caracteres = int(input('Número de caracteres da senha: '))
            for quantidade in range(quantidade_caracteres):
                lista1.append(self.letra_aleatoria())
            return lista1

    def somente_letra_e_numeros(self):
            lista1 = []
            quantidade_caracteres = int(input('Número de caracteres da senha: '))
            for quantidade in range(quantidade_caracteres):
                seletor = self.escolha_tipo_letra_e_numero()
                if seletor == '0':
                    lista1.append(self.letra_aleatoria())
                elif seletor == '1':
                    lista1.append(self.numero_aleatorio())
            return lista1

    def todos_os_caracteres(self):
            lista1 = []
            quantidade_caracteres = int(input('Número de caracteres da senha: '))
            for quantidade in range(quantidade_caracteres):
                seletor = self.escolha_tipo()
                if seletor == '0':
                    lista1.append(self.letra_aleatoria())
                elif seletor == '1':
                    lista1.append(self.simbolo_aleatorio())
                elif seletor == '2':
                    lista1.append(self.numero_aleatorio())
            return lista1

    def selecao_de_tipo(self, selecao):
            if selecao == 'l':
                senha_lista = self.somente_letras()
            elif selecao == 'n':
                senha_lista = self.somente_numeros()
            elif selecao == 'ln':
                senha_lista = self.somente_letra_e_numeros()
            elif selecao == 'lns':
                senha_lista = self.todos_os_caracteres()
            else:
                print('Valor invalido')
                exit()

            return senha_lista


Gerador_senha()
