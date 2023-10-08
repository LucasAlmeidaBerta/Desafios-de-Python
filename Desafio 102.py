def factorial(num, show=False):
    """
    -> Imprime a fatorial de um número proposto.
    :param num: valor para realizar a fatorial
    :param show: True para mostrar a sequência da fatorial, False para não mostrar
    :return: Retorna o valor da fatorial
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(f'{c} -> ', end='')
    return f


print(factorial(5, show=True))
print(help(factorial))
