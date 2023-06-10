print('Gerador de PA')
print('=+' * 10)
n = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
termo = n
cont = 1
total = 0
maistermo = 10
while maistermo != 0:
    total += maistermo
    while cont <= total:
        print(' {} ,'.format(termo), end='')
        termo += r
        cont += 1
    maistermo = int(input('Quantos mais termos gostaria de ver? '))
print("Acabou")