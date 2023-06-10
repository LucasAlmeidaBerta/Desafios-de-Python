v1 = int(input('Insira um valor inteiro para comparação: '))
v2 = int(input('Insira outro valor inteiro para comparação: '))
if v1 > v2:
    print('{} é maior que {}. '.format(v1, v2))
elif v1 < v2:
    print('{} é maior que {}'.format(v2, v1))
else:
    print('{} é igual a {}.'.format(v1, v2))
