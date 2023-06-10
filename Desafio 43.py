p = float(input('Informe seu peso em kg: '))
h = float(input('Informe sua altura em metros: '))
imc = p / h ** 2
print('Seu IMC é: {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do  peso!')
elif 18.5 < imc < 25:
    print('Você está no peso ideal.')
elif 25 < imc < 30:
    print('Você está com sobrepeso!')
elif 30 < imc < 40:
    print('Você está obeso!')
else:
    print('Você está com obesidade mórbida!')
