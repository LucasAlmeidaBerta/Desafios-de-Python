from time import sleep


def maior(*num):
    print(f'Foram informados os valores {num} ', end='')
    print(f'ao todo {len(num)} valores')
    if len(num) > 0:
        print(f'O maior número da Lista foi {max(num)}.')
    elif len(num) == 0:
        print('O maior número da Lista foi 0.')
    print('-='*31)
    sleep(0.3)


# main
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
