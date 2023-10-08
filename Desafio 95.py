jogadores = list()
cad = dict()
gols = list()
total = 0
while True:
    cad['nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou?'))
    for i in range(0, partidas):
        gols.append(int(input(f'Quantos gols ele fez na partida {i}: ')))
        cad['gols'] = gols[:]
        total += gols[i]
        cad['total'] = total
    jogadores.append(cad.copy())
    cad.clear()
    gols.clear()
    resp = str(input('Deseja continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('=-'*30)
print(f'{"N°":>3} {"Nome":<15} {"Gols"} {"Total":>10}')
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end ='')
    print()
while True:
    cod = int(input('Insira o número do jogador que deseja mostrar os dados? (999 para parar)'))
    if cod == 999:
        print('PROGRAMA ENCERRADO!!!')
        break
    if cod in range(0, len(jogadores)):
        for j, g in enumerate(jogadores[cod]["gols"]):
            print(f'No Jogo {j+1} fez {g} gols')
    else:
        print('Insira uma opção válida!')
