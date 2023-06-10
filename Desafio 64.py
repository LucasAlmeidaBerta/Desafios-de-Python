"""n = 0
cont = -1
soma = 0
while n != 999:
    n = int(input('Insira um número, (999 para parar): '))
    cont += 1
    soma += n
print("Você digitou {} Números e a soma é {}".format(cont, soma - 999))"""

n = cont = soma = 0
n = int(input('Insira um número, (999 para parar): '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Insira um número, (999 para parar): '))
print("Você digitou {} Números e a soma é {}.".format(cont, soma))
