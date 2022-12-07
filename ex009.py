num = int(input('Digite um número para sua tabuada: '))
print('=' * 18)
print('Tabuada de {}'.format(num))

print('{} x {} = {}'.format(num, 0, num*0))
print('{} x {} = {}'.format(num, 1, num*1))
print('{} x {} = {}'.format(num, 2, num*2))
print('{} x {} = {}'.format(num, 3, num*3))
print('{} x {} = {}'.format(num, 4, num*4))
print('{} x {} = {}'.format(num, 5, num*5))
print('{} x {} = {}'.format(num, 6, num*6))
print('{} x {} = {}'.format(num, 7, num*7))
print('{} x {} = {}'.format(num, 8, num*8))
print('{} x {} = {}'.format(num, 9, num*9))
print('{} x {} = {}'.format(num, 10, num*10))
print('=' * 18)

#tauada com while
valor = int(input('Entre com um número para saber a tabuada: '))
aux = 0 #começa do zero
print('*' * 18)
print('Tabuada de {}'.format(valor))
print('*' * 18)
while(aux <= 10):
  print('{} x {} = {}'.format(valor, aux, (aux * valor)))
  aux = aux + 1
print('*' * 18)  
print('-' * 18)
print('Ahavadev')
  

