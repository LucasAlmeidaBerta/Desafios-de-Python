lista = []
for v in range(0, 5):
    lista.append(int(input('Insira um valor: ')))
print(lista)
print(f'O maior número da lista digitado foi: {max(lista)} na {lista.index(max(lista)) + 1}° posição')
print(f'O menor número da lista digitado foi: {min(lista)} na {lista.index(min(lista)) + 1}° posição')
