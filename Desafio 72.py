numeros = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input("Insira o número que deseja ver (0 - 20): "))
    if 0 <= n <= 20:
        print(numeros[n])
        break
    else:
        print('###ERRO###')
