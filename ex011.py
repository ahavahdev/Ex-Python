largura = float(input("Digite a largura da parede "))
altura = float(input("Digite a altura da parede "))
area = largura * altura

print('Sua parede tem {}m de altura e {}m de largura e sua área é {}m2 de '.format(altura, largura, area))
#a cada 2m eu preciso de 2 lt de tinta
tinta = area/2
print('Você vai precisar de {} L de tinta'. format(tinta))
