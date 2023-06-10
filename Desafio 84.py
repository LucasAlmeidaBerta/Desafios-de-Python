pessoas = list()
grupo = list()
pesados = list()
leves = list()
maior = menor = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso(kg): ')))
    if len(grupo) == 0:
        maior = menor = pessoas[1]
    else:
        if pessoas[1] > maior:
            maior = pessoas[1]
        elif pessoas[1] < menor:
            menor = pessoas[1]
    grupo.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Deseja inserir uma nova pessoa? (S/N)')).upper()
    if resp in 'Ss':
        continue
    else:
        break
print(f'Você cadastrou {len(grupo)} pessoas')
print(f'O maior peso foi de {maior} kg de ', end='')
for p in grupo:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi de {menor} kg')
for p in grupo:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
