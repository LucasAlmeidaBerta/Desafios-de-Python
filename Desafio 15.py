d = int(input('Quanto dias o veículo foi locado? '))
km = float(input('Quantos km foram percorridos? '))
c = d*60+0.15*km
print('O veículo foi alugado por {} dias e foi percorrido {} km, \nficando o total a pagar de R${:.2f} '.format(d, km, c))