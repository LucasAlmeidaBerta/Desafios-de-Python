n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda  nota: '))
nf = (n1 + n2) / 2
if nf < 5:
     print('Você foi reprovado. ')
elif 5 < nf < 6.9:
    print('Você está de recuperação. ')
else:
    print('Você foi aprovado! ')
