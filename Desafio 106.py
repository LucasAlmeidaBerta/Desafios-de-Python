from time import sleep
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[7;30m'
     )


def ajuda(comando):
    tit(f'Acessando o manual do comando \'{comando}\'', 2)
    print(c[3], end='')
    help(comando)
    print(c[0], end='')
    sleep(2)


def tit(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('=' * tam)
    print(f'  {msg}')
    print('=' * tam)
    print(c[0], end='')
    sleep(2)


comando = ''
while True:
    tit('Sistema de ajuda PyHelp', 2)
    comando = str(input('Função ou Biblioteca -> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
tit('Até Logo!', 1)
