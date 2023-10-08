from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 Valores: ', end='')
    for n in range(0, 5):
        lista.append(randint(1, 10))
        print(f'{lista[n]} ', end='')
        sleep(0.3)
    print('PRONTO!')


def somapar():
    soma = 0
    for n in range(0, 5):
        if lista[n] % 2 == 0:
            soma += lista[n]
    print(f'A soma dos valores pares da lista é de {soma}')


# main
lista = list()
sorteia()
somapar()
