from math import hypot
co = float(input('Insira o valor do cateto oposto '))
ca = float(input('Insira o valor do cateto adjacente '))
h = hypot(co, ca)
print('O valor da hipotenusa é igual a: ', h)