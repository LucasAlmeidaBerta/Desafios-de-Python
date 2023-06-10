print('Insira dois números para realização da operação matemática de sua prefêrencia!')
x = int(input('Insira o primeiro número: '))
y = int(input('Insira o segundo número: '))
c = 0
while c != 5:
    c = int(input('Insira o número da opção desejada: \n[1] = Soma\n[2] = Multiplicação\n[3] = Maior\n[4] = Novos Números\n[5] = Sair do programa. '))
    if c == 1:
        r = x + y
        print('A soma de {} e de {} é igual a {}'.format(x, y, r))
    elif c == 2:
        m = x * y
        print('A multiplicação entre {} e {} é igual a {}'.format(x, y, m))
    elif c == 3:
        if x > y:
            maior = x
        else:
            maior = y
        print('O maior número é {}'.format(maior))
    elif c == 4:
        x = int(input('Insira o primeiro número: '))
        y = int(input('Insira o segundo número: '))
    else:
        print('Opção inválida, tente novamente')
print('Fim do programa!')