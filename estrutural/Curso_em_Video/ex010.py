'''
Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa 
tem na carteira e mostre quantos dólares ela pode comprar.
'''
dolar = 5.16
reais = float(input('Digite quanto dinheiro você tem na carteira: '))
brlusd = reais/dolar
print('Com R$ {} você consegue comprar US$ {:.2f}'.format(reais,brlusd))

