n = int(input('Insira um número de 0 a 9999: '))
u = n % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('A unidade do seu número é {}'.format(u))
print('A Dezena do seu número é: {}'.format(d))
print('A centena do seu número é: {}'.format(c))
print('O milhar do seu número é: {}'.format(m))
