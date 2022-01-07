'''
Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá 
escrever na tela se o usuário venceu ou perdeu.
'''
import random

pc = random.randint(0, 5)
print('-=-' * 20)
print('Estou pensando em um numero entre 0 e 5, tente advinhar...')
print('-=-' * 20)
num = int(input('Em qual numero eu pensei? '))

if pc == num:
	print('voce venceu eu pensei em {}'.format(pc))
else:
	print('voce perdeu, eu pensei em {}'.format(pc))
