frase = str(input('Insira sua frase: ')).upper().strip()
print('A letra A foi encontrada {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na : {}° posição'.format(frase.find('A')+1))
print('A Ultima letra A na : {}° posição'.format(frase.rfind('A')+1))
