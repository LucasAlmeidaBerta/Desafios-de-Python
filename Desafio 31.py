d = int(input('Qual a distância da sua viagem em km: '))
if d >= 201:
    c1 = d * 0.45
    print('O custo da sua viagem será de R${:.2f}'.format(c1))
else:
    c2 = d * 0.5
    print('O custo da sua viagem será de R${:.2f}'.format(c2))
