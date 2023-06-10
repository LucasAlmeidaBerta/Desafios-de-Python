media = 0
idadevelho = 0
nomevelho = 0
mulheres = 0
for c in range(1, 5):
    nome = str(input('Insira o nome da {}° pessoa: '.format(c)))
    idade = int(input('Insira a idade da {}° pessoa: '.format(c)))
    sexo = str(input('Insira o sexo [M/F] da {}° pessoa: '.format(c)))
    media += idade
    if c == 1 and sexo in 'Mm':
        idadevelho = idade
        nomevelho = nome
    if idade > idadevelho and sexo in 'Mm':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <= 20:
        mulheres += 1
print('O homem mais velho tem {} e se chama {}'.format(idadevelho, nomevelho))
print('A média da idade do grupo é {}'.format(int(media / 4)))
print('A quantidade de mulheres menores de 20 anos é de {}'.format(mulheres))
