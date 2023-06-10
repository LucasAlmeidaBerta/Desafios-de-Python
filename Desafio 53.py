f = str(input('Insira sua frase: ')).strip().upper()
fdividida = f.split()
junto = ''.join(fdividida)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Este é um palíndromo.')
else:
    print('Este não é um palíndromo.')

