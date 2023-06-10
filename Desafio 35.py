l1 = float(input('Insira o comprimento do primeiro lado do triângulo: '))
l2 = float(input('Insira o comprimento do segundo lado do triângulo: '))
l3 = float(input('Insira o comprimento do terceiro lado do triângulo: '))
if l2 - l3 < l1 < l2 + l3:
    print('Este é um triângulo!')
else:
    print('Este não é um triângulo!')
