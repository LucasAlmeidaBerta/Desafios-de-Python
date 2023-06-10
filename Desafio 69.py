contm = contf = contmaior = r = 0
while True:
    r = " "
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Insira o sexo da pessoa: [M/F]")).upper().split()[0]
    idade = int(input("Insira a idade da pessoa: "))
    if sexo == "M":
        contm += 1
    if sexo == "F" and idade < 20:
        contf += 1
    if idade > 18:
        contmaior += 1
    while r not in "SN":
        r = str(input("Você deseja continuar? [S/N] ")).upper().strip()[0]
    if r == "N":
        break
print(f"a) O total de pessoas maiores de idade é de {contmaior}")
print(f"b) O número de homens cadastrados foi de {contm}")
print(f"c) O número de mulheres menores de 20 anos foi de {contf}")
