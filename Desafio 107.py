from desafio107 import moeda
valor = float(input('Insira o Valor: RS'))
print(f'A metade de {valor} é {moeda.metade(valor)}')
print(f'O dobro de {valor} é {moeda.dobro(valor)}')
print(f'Aumentado 10%, temos {moeda.aumentar(valor)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(valor)}')
