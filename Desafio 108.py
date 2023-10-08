from desafio108 import moeda
valor = float(input('Insira o Valor: RS'))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentado 10%, temos {moeda.moeda((moeda.aumentar(valor)))}')
print(f'Diminuindo 13%, temos {moeda.moeda(moeda.diminuir(valor))}')
