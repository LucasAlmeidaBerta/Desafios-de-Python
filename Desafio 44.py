print('{:-^50}'.format(' BERTAS GROCERY '))
v = float(input('Insira o valor do produto: R$'))
c = int(input('Para pagamento em dinheiro ou cheque digite 1.\nPara pagamento à vista no cartão digite 2.\nPara '
              'Pagamento até 2x no cartão digite 3.\nPara pagamento em 3x ou mais no cartão digite 4\nSua opção: '))
if c == 1:
    print('O valor a pagar será de R${}.'.format(v - v * 0.1))
elif c == 2:
    print('O valor a pagar será de R${}.'.format(v - v * 0.05))
elif c == 3:
    print('O valor a pagar será de R${}.'.format(v))
elif c == 4:
    print('O valor a pagar será de R${}.'.format(v + v * 0.2))
else:
    print('Insira uma opção válida')
