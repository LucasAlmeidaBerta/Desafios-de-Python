dic = {}
dic['nome'] = str(input('Nome: '))
dic['media'] = float(input('Média: '))
print(f'O nome é {dic["nome"]}')
print(f'A média é igual a {dic["media"]}')
if dic['media'] >= 6:
    print(f'{dic["nome"]} foi Aprovado!')
else:
    print(f'{dic["nome"]} foi Reprovado.')
