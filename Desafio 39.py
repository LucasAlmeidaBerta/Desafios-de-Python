from datetime import date
atual = date.today().year
nasc = int(input('Insira seu ano de nascimento: '))
idade = atual - nasc
saldo = idade - 18
if idade > 18:
    print('Ja passou o tempo de se alistar fazem {} anos!'.format(saldo))
elif idade == 18:
    print('Você deve se alistar imediatamente!')
else:
    print('Ainda não está na hora de se alistar faltam {} anos!'.format(saldo))
