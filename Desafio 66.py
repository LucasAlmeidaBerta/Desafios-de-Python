cont = soma = n = 0
while True:
    n = int(input('Insira um número, (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print("Você digitou {} Números e a soma é {}.".format(cont, soma))
