lista = []
lista.append(int(input('Insira um valor na lista:')))
for v in range(0, 4):
    n = (int(input('Insira um valor na lista: ')))
    if n > max(lista):
        lista.insert(5, n)
    elif n < min(lista):
        lista.insert(0, n)
print(lista)
