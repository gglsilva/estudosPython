'''
Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço
da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
'''

km = float(input('Qual a distância da sua viagem? '))

if km <= 200:
	valor = km * 0.50
else:
	valor = km * 0.45

print('voce esta prestes a começar uma viagem de {}.\nO valor da passagem será de R$ {}'.format(km, valor))
