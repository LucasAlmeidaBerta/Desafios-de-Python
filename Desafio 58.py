from random import randint
c = randint(0, 10)
print('Você precisa acertar o valor correto para ganhar do computador')
r = int(input('Insira um número inteiro de 0 a 10: '))
s = 1
while r != c:
    r = int(input('Você errou, insira um número novamente!'))
    s += 1
print('CORRETO!!! \nVocê precisou de {} chances para acertar!'.format(s))
