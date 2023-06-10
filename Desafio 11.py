l = float(input('Insira a largura da parede em metros: '))
h = float(input('Insira a altura da parede em metros'))
v = (l*h)/2
print('Sua parede tem {:.2f} m², Será gasto {:.3f} litros'.format(l*h, v))
