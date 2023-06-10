from random import randint
contpar = contimpar = contv = 0
while True:
    p = int(input("Escolha entre um número par ou um número ímpar: "))
    c = randint(0, 11)
    soma = p + c
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? ")).strip().upper()[0]
    print(f"Você jogou {p} e o computador jogou {c} a soma foi igual a {soma}.")
    if tipo == "P" and soma % 2 == 0:
        print("Deu Par e Você ganhou!")
        contv += 1
    elif tipo == "I" and soma % 2 >= 1:
        print("Deu ímpar e você ganhou!")
        contv += 1
    else:
        print("Você perdeu! ")
        break
print(f"Você ganhou {contv} vezes")
