matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somacoluna = maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            soma += matriz[linha][coluna]
        if coluna == 2:
            somacoluna += matriz[linha][coluna]
        if matriz[1][coluna] > maior:
            maior = matriz[1][coluna]
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares da matriz é igual a {soma}')
print(f'Os valores somados da terceira coluna é igual a {somacoluna}')
print(f'O maior valor da segunda linha digitado foi {maior}')
