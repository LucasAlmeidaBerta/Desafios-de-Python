lista = []
while True:
    resp = str(input('Deseja adicionar um número na lista? [S/N]').upper())
    if resp == 'S':
        n = int(input('Digite um valor para adicionar a lista: '))
        if n in lista:
            print('Este valor já foi inserido, tente novamente!')
        elif n not in lista:
            lista.append(n)
    elif resp == 'N':
        break
    else:
        print('Insira uma respota válida')
print(f'Foram adicionado {len(lista)} números a lista!')
lista.sort(reverse=True)
print(lista)
if 5 in lista:
    print('O valor 5 está presente na lista')
