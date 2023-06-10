"""while True:
    n = int(input('Insira o número que deseja ver a tabuada: '))
    if n < 0:
        break
    print(f"1 x {n} = {n}\n2 x {n} = {n*2}\n3 x {n} = {n*3}\n4 x {n} = {n*4}\n5 x {n} = {n*5}\n6 x {n} = {n*6}\n7 x {n} = {n*7}\n8 x {n} = {n*8}\n9 x {n} = {n*9}")"""
while True:
    n = int(input("Insira um número que deseja ver a tabuada: "))
    if n < 0:
        break
    for c in range(1,11):
        print(f"{n} x {c} = {n*c}")
print("Acabou! ")
