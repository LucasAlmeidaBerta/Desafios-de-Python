cad = list()
femininos = list()
pessoa = dict()
total = 0
while True:
    pessoa['nome'] = (str(input('Nome: ')))
    pessoa['sexo'] = (str(input('Sexo: [M/F] '))).upper()
    while pessoa['sexo'] not in 'mMfF':
        print('ERRO!!! Por favor, digite apenas M ou F.')
        del pessoa['sexo']
        pessoa['sexo'] = (str(input('Sexo: [M/F] ')))
    if pessoa['sexo'] in 'Ff':
        femininos.append(pessoa.copy())
    pessoa['idade'] = (int(input('Idade: ')))
    total += pessoa['idade']
    resp = (str(input(print('Deseja continuar? [S/N] '))))
    while resp not in 'SN':
        print('ERRO!!! Por favor, digite apenas S ou N.')
        resp = (str(input(print('Deseja continuar? [S/N] '))))
    if resp == 'N':
        cad.append(pessoa.copy())
        break
    if resp == 'S':
        cad.append(pessoa.copy())
print(pessoa)
print(f'A) Ao todo temos {len(cad)} pessoas cadastradas.')
print(f'B) A média de idade é de {total/(len(cad))} Anos.')
print('C) As mulheres cadastradas foram: ', end='')
for c in range(0, len(femininos)):
    print(f'{femininos[c]["nome"]}', end=' ')
print('\nD) As pessoas com idade acima da média são: ', end='')
for i in range(0, len(cad)):
    if cad[i]['idade'] >= (total/(len(cad))):
        print(cad[i]['nome'], end=' ')
