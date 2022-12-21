salario = float(input('Qual é o salário do funcionário '))
aumento = float(input('Qual a porcentagem de aumento? '))

novo = salario + (salario * aumento / 100)
print('O funcionário que ganhava R$ {:.2f}, com {:.2f} % de aumento agora ganha R$ {:.2f} '.format(salario, aumento, novo))



