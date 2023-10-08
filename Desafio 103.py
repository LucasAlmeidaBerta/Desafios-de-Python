def ficha(jogador="<desconhecido>", gols=0):
    print(f'O jogador {jogador} fez {gols} gols no compeonato.')


nome = str(input('Insira o nome do jogador: '))
gol = str(input('Insira o número de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)
