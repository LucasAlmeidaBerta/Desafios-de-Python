s = (str(input('Insira seu sexo [M/F]'))).upper().strip()
while s not in 'MF':
    s = (str(input('Insira um sexo válido [M/F]'))).upper().strip()
print('Fim')
