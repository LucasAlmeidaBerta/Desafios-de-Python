from math import radians, sin, cos, tan
a = float(input('Informe um ângulo qualquer '))
s = sin(radians(a))
print('O ângulo de {} tem seu seno de {:.2f}'.format(a, s))
c = cos(radians(a))
print('O Ângulo de {} tem seu cosseno de {:.2f}'.format(a, c))
t = tan(radians(a))
print('O Ângulo de {} tem sua tangente de {:.2f}'.format(a, t))


