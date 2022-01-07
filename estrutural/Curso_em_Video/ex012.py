'''
Exercício Python 012: Faça um algoritmo que leia o preço de um produto e 
mostre seu novo preço, com 5% de desconto.
'''

preco_a = float(input('Digite o preço do produto: '))

preco_d = preco_a -(preco_a* 0.05)
print('O Preço sem desconto é R$ {}, com desconto de 5% vai fica R$ {}'.format(preco_a,preco_d))
