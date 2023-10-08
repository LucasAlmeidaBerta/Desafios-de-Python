def leiaint(numero):
    while True:
        try:
            nume = int(input(numero))
        except (ValueError, TypeError):
            print('Você errou o tipo de dado a ser inserido')
        except KeyboardInterrupt:
            print('Você optou por sair do programa')
        else:
            return nume


def leiafloat(numero):
    while True:
        try:
            nume = float(input(numero))
        except (ValueError, TypeError):
            print('Você errou o tipo de dado a ser inserido')
        except KeyboardInterrupt:
            print('Você optou por sair do programa')
        else:
            return nume


num2 = leiafloat('Insira um número real: ')
print(f'Você acabou de digitar {num2}')
num = leiaint('Insira um valor inteiro: ')
print(f'Você acabou de digitar {num}')
