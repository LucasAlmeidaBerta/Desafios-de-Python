from datetime import datetime
dic = dict()
dic['nome'] = str(input('Qual é seu nome? '))
nasc = int(input('Ano de nascimento: '))
dic['idade'] = datetime.now().year - nasc
dic['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dic['ctps'] != 0:
    dic['contratação'] = int(input('Ano de contratação: '))
    dic['salario'] = float(input('Salario: R$'))
    dic['aposentadoria'] = dic['idade'] + ((dic['contratação'] + 35) - datetime.now().year)
for k, v in dic.items():
    print(f'  {k} tem o valor {v}')
