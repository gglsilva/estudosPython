'''
Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 
80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km 
acima do limite.
'''

velocidade = float(input('Digite a velocidade do carro: '))
vl_acima = velocidade - 80
valor_multa = vl_acima * 7


if velocidade > 80:
	print('voce foi multado, seu carro estava {} acima da velocidade permitida'.format(vl_acima))
	print('o valor da multa foi de R${}'.format(valor_multa))
elif velocidade <= 80:
	print('voce não foi multado')
