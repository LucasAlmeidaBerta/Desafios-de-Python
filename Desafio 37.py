n = int(input('Insira um número inteiro para conversão: '))
b = int(input('Para binário digite 1,\nPara Octadecimal digite 2,\nPara Hexadecimal digite 3\nSua Opção: '))
if b == 1:
    print('{} convertido para binário é {}.'.format(n, bin(n)[2:]))
elif b == 2:
    print('{} convertido para Octadecimal é {}'.format(n, oct(n)[2:]))
elif b == 3:
    print('{} convertido para Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Insira uma opção válida')
