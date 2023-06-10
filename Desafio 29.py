v = float(input('Insira a velocidade em km/h do veículo: '))
c = (v - 80) * 7
if v >= 80:
    print('Você excedeu o limite de velocidade da via!')
    print('Você terá que pagar R${} de multa'.format(c))
else:
    print('Você estava dentro do limite da via!')
