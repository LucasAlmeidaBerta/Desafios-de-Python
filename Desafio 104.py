def leiaint(numero):

    while True:
        numero = str(input('Insira um número: '))
        if numero.isnumeric() and int(numero):
            return numero
        else:
            print('ERRO! Digite um número válido!')


num = leiaint('Insira um número: ')
print(f'Você acabou de digitar {num}')
