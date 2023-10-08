from desafio109 import moeda
valor = float(input('Insira o Valor: RS'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')
print(f'Aumentado 10%, temos {(moeda.aumentar(valor, True))}')
print(f'Diminuindo 13%, temos {(moeda.diminuir(valor, True))}')
