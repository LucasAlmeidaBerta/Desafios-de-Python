n1 = int(input("Insira o primeiro valor: "))
n2 = int(input("Insira o segundo valor: "))
n3 = int(input("Insira o terceiro valor: "))
n4 = int(input("Insira o quarto valor: "))
lista = (n1, n2, n3, n4)
cont = 0
if n1 or n2 or n3 or n4 == 9:
    cont += 1
print(lista)
print(f'O número 9 apareceu {cont} vezes')
# print(f'O número 9 apareceu {lista.count(9)} vezes')
if 3 in lista:
    print(f'O número 3 apareceu na {lista.index(3) + 1}° posição')
print('Os números pares digitados foram: ', end= ' ')
for n in lista:
    if n % 2 == 0:
        print(n, end=', ')
