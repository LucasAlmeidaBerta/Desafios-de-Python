from datetime import date
atual = date.today().year
cont = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input('Insira o ano de nascimento da {}° pessoa: '.format(c)))
    if atual - ano >= 21:
        cont += 1
    else:
        cont2 += 1
print('O número de pessoas maiores de idade são {} e de menores são {}'.format(cont, cont2))
