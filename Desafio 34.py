s = float(input('insira o valor do seu salário: R$'))
if s > 1250.00:
    sv = s + s * 0.1
    print('Seu salário com aumento ficou R${}'.format(sv))
else:
    sv2 = s + s * 0.15
    print('Seu salário com aumento ficou R${}'.format(sv2))
