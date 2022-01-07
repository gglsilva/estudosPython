'''
Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não 
pode exceder 30% do salário ou então o empréstimo será negado.
'''

casa = float(input('Qual o valor da casa que voce predente financiar? R$ '))
salario = float(input('Qual o seu salario mensal? R$'))
anos = float(input('Em quantos anos predente financiar a casa? '))

vl_minimo = casa / (anos * 12)
p_salario = (salario * 0.30)

if vl_minimo <= p_salario:
	print('Para pagar R$ {} em {} anos o valor minimo das parcelas deverar ser {}'.format(casa, anos, vl_minimo))
	print('O Empretimo poderar ser concedido')
else:
	print('Para pagar R$ {} em {} anos o valor minimo das parcelas deverar ser {:.2f}'.format(casa, anos, vl_minimo))
	print('O Empretimo Não poderar ser concedido')