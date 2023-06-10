from datetime import date
atual = date.today().year
nasc = int(input('Qual o ano do seu nascimento? '))
classe = atual - nasc
print('A idade do atleta é {} anos.'.format(classe))
if classe <= 9:
    print('A categoria deste aluno é MIRIM!')
elif 9 < classe <= 14:
    print('A categoria deste aluno é INFANTIL!')
elif 14 < classe <= 19:
    print('A categoria deste aluno é JÚNIOR!')
elif 19 < classe <= 25:
    print('A categoria deste aluno é SÊNIOR!')
else:
    print('A categoria deste aluno é MASTER!')
