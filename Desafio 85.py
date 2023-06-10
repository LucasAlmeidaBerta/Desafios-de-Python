numeros = [[], []]
valor = 0
for v in range(0, 7):
    valor = int(input(f'Digite o {v+1}° valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print(numeros)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares são: {numeros[0]}')
print(f'Os números impares são: {numeros[1]}')
