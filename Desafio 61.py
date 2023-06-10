print('Gerador de PA')
print('=+' * 10)
n = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
for c in range(n, n + 10 * r, r):
    print(' {} ,'.format(c), end='')
print('\nGerador de PA')
print('=+' * 10)
n = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
termo = n
cont = 1
while cont <= 10:
    print(' {} ,'.format(termo), end='')
    termo += r
    cont += 1
