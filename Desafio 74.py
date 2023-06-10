from random import randint
print('Os números sorteador foram', end=' ')
lista = (randint(0, 10), randint(0, 10), randint(0, 10),
          randint(0, 10), randint(0, 10))
print(lista)
print(f'O Maior número sorteado foi {max(lista)}')
print(f'O menor número sorteado foi {min(lista)}')
