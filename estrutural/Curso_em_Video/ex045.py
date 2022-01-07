'''
Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
'''
from random import choice
from time import sleep

def imprimi():
	lista = ['JO', 'kEN', 'PO!!!']
	for i in lista:
		print(i)
		sleep(1)


def ganhador(pc , op):
	if pc == 'Pedra' and op == 'Tesoura':
		print('O computador venceu!')
	elif pc == 'Pedra' and op == 'Papel':
		print('você venceu, Parabéns!!!')
	elif pc == 'Pedra' and op == 'Pedra':
		print('Deu Empate!!!')

	if pc == 'Papel' and op == 'Pedra':
		print('O computador venceu!')
	elif pc == 'Papel' and op == 'Tesoura':
		print('você venceu, Parabéns!!!')
	elif pc == 'Papel' and op == 'Papel':
		print('Deu Empate!!!')

	if pc == 'Tesoura' and op == 'Papel':
		print('O computador venceu!')
	elif pc == 'Tesoura' and op == 'Pedra':
		print('você venceu, Parabéns!!!')
	elif pc == 'Tesoura' and op == 'Tesoura':
		print('Deu Empate!!!')	


lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)

op = int(input('''Sua Opção:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
Qual a Sua Jogada?'''))

imprimi()
print('='*20)
print('O computador jogou {}'.format(pc))
print('O jogador jogou {}'.format(lista[op]))
print('='*20)
print(ganhador(pc, lista[op]))

