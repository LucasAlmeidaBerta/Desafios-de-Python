from time import sleep


def cont(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i > f and p > 0:
        p *= -1
        f -= 2
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for c in range(i, f+1, p):
        print(c, end=' ')
        sleep(0.3)
    print('FIM!')


# main
cont(1, 10, 1)
cont(10, 0, 2)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
cont(inicio, fim, passo)
