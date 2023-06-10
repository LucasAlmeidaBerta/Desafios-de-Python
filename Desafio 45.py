from random import randint
r = int(input('Escolha entre\n[0]Pedra\n[1]Papel\n[2]Tesoura\nSua opção: '))
lista = ('pedra', 'papel', 'tesoura')
c = randint(1, 2)
print('Você jogou {} e o computador jogou {}.'.format(lista[r], lista[c]))
if c == 0:
    if r == 0:
        print('Empate')
    elif r == 1:
        print('Você ganhou!')
    elif r == 2:
        print('Você perdeu!')
elif c == 1:
    if r == 0:
        print('Você perdeu')
    elif r == 1:
        print('Empate')
    elif r == 2:
        print('Você ganhou!')
elif c == 2:
    if r == 0:
        print('Você ganhou!')
    elif r == 1:
        print('Você perdeu')
    elif r == 2:
        print('Empate')
