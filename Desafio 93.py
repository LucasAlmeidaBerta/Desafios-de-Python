cad = dict()
gols = list()
total = 0
cad['nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou?'))
for i in range(0, partidas):
    gols.append(int(input(f'Quantos gols ele fez na partida {i}: ')))
    cad['gols'] = gols
    total += gols[i]
    cad['total'] = total
print(cad)
print('=-'*30)
for k, v in cad.items():
    print(f'O Campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {cad["nome"]} jogou {partidas} partidas')
for k, v in enumerate(gols):
    print(f'==> Na {k+1}° partida fez {v} gols!')
