from random import randint
from time import sleep
numeros = []
sorteados = []
lista = []
temp = []
for num in range(1, 61):
    numeros.append(num)
quant = int(input('Quantos jogos deseja sortear? '))
print(f'{"=-"*3} Sorteando {quant} jogos para você! {"=-"*3}')
for jogos in range(0, quant):
    cont = 0
    while cont != 6:
        numero = randint(0, 60)
        if numero not in temp:
            temp.append(numero)
            cont += 1
    sorteados.append(temp[:])
    temp.clear()
    print(f'Jogo {jogos+1}: {sorteados[jogos]}')
    sleep(1)
print(f'{"=-"*5} < Boa Sorte! > {"=-"*5}')
 