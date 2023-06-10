r = soma = cont = maior = 0
menor = 1000
while r != "N":
    n = int(input("Insira um número: "))
    cont += 1
    soma += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    r = str(input("Quer continuar? [S/N] ").upper())
print(f"A média entre os números digitados é: {soma/cont}")
print("O maior valor digitado foi: {}.".format(maior))
print("O menor valor digitado foi: {}".format(menor))
