import random
lista = [0, 1, 2, 3, 4, 5]
nc = random.choice(lista)
n = int(input('Insira um Número inteiro de 0 a 5: '))
if n == nc:
    print('Parabens, você acertou o número!')
else:
    print('Você errou, tente outra vez. o número era {}'.format(nc))

