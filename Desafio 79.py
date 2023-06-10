lista = []
while True:
    resp = str(input('Deseja acionar um número na lista? [S/N]').upper())
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
lista.sort()
print(lista)
