v = float(input('Qual valor será financiado? '))
s = float(input('Qual é o seu salário? '))
t = int(input('Em quantos meses gostaria de pagar o valor financiado? '))
vm = v/t
if vm < 0.3*s:
    print('Crédito aprovado! \nO valor da parcela ficará {:.2f} em {} meses'.format(vm, t))
else:
    print('Infelizmente não foi possível aprovar o crédito.')
