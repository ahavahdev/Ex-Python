preço = float(input('Qual é o preço do produto? R$ '))
porcentagem = float(input('Digite quantos porcento quer dar de desconto '))

novo = preço - (preço * 5 / 100) # 5% #colocando a porcentagem no cod
novo2 = preço - (preço * porcentagem /100) #usuário digitando a porcentagem


print('O preço do produto que custava R$ {:.2f} agora custa R$ {:.2f}'.format(preço, novo))
print('O preço do produto que custava R$ {:.2f} agora custa R$ {:.2f} com {} % de desconto'.format(preço, novo2, porcentagem))



