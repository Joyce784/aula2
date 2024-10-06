#Crie um programa que peça ao usuário o preço original de um 
# produto e
#a quantidade comprada. Use if para verificar se a quantidade 
# é maior que
#10 para aplicar um desconto de 10% sobre o total.

preço = int(input('Digite o preço do produto:'))
unidade = int(input('Quantas unidades:'))
total = preço * unidade
if unidade >=11:
    print('{}'.format(total/10*9))
else:
    print(total)