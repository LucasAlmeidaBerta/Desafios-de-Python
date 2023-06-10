t = int(input('Quantos termos deseja da sequência de Fibonacci deseja ver? '))
t1 = 0
t2 = 1
cont = 2
print('{} -> {} -> '.format(t1, t2), end='')
while t > cont:
    t3 = t1 + t2
    print('{} -> '.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print('Fim')