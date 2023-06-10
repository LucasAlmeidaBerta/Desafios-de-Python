soma = cont = barato = contp = pbarato = 0
while True:
    nome = str(input("Qual o nome do produto comprado? "))
    valor = int(input("Qual o valor pago no produto? "))
    soma += valor
    contp += 1
    r = " "
    if valor >= 1000:
        cont += 1
    if contp == 1:
        barato = valor
        pbarato = nome
    else:
        if valor < barato:
            pbarato = nome
            barato = valor
    while r not in "SN":
        r = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
    if r == "N":
        break
print(f"O valor total gasto na compra de {contp} produtos foi de R${soma}, {cont} produtos custaram mais de R$1000,00 e produto mais barato comprado foi {pbarato} por R${barato}")
