lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    resp = str(input('Deseja conitnuar? [S/N] '))
    lista.append([nome, [nota1, nota2], media])
    if resp in 'Nn':
        break
print('='*30)
print('N°  Nome         Média')
for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    opcao = int(input('Deseja ver a nota de qual aluno? (999 para interromper): '))
    if opcao == 999:
        break
    elif opcao <= len(lista) - 1:
        print(f'As notas de {lista[opcao][0]} são {lista[opcao][1]}')
