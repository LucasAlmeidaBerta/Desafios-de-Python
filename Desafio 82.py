lista = []
listapar = []
listaimpar = []
while True:
    resp = str(input('Deseja acionar um número na lista? [S/N]').upper())
    if resp == 'S':
        n = int(input('Digite um valor para adicionar a lista: '))
        if n in lista:
            print('Este valor já foi inserido, tente novamente!')
        elif n not in lista:
            lista.append(n)
            if n % 2 == 0:
                listapar.append(n)
            else:
                listaimpar.append(n)
    elif resp == 'N':
        break
    else:
        print('Insira uma respota válida')
print(f'A lista gerada foi: {lista}')
print(f'A lista de números pares é: {listapar}')
print(f'A lista de números impares é: {listaimpar}')
