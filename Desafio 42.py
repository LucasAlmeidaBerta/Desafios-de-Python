l1 = float(input('Insira o comprimento do primeiro lado do triângulo: '))
l2 = float(input('Insira o comprimento do segundo lado do triângulo: '))
l3 = float(input('Insira o comprimento do terceiro lado do triângulo: '))
if l2 - l3 < l1 < l2 + l3:
    print('Este é um triângulo!')
    if l1 == l2 == l3:
        print('Este é um triângulo equilátero!')
    elif l1 != l2 != l3 != l1:
        print('Este é um triângulo escaleno!')
    else:
        print('Este é um triângulo isóceles')
else:
    print('Este não é um triângulo!')
