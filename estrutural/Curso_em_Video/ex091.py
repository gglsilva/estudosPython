'''
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses 
resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o 
maior número no dado.
'''
'''Meu Código
from random import randint
dado = {}
dado['jogador1'] = randint(1, 6)
dado['jogador2'] = randint(1, 6)
dado['jogador3'] = randint(1, 6)
dado['jogador4'] = randint(1, 6)
for k, v in dado.items():
	print(f'{k} tirou {v} no dado.')
print('-=' * 30)
print('   === Ranking dos Jogadores ===')
cont = 1
for i in sorted(dado, key = dado.get, reverse=True):
	print(f'	{cont}º lugar:{i} com {dado[i]}')
	cont += 1
'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
'jogador2': randint(1, 6),
'jogador3': randint(1, 6),
'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados:')
for k, v in dado.items():
	print(f'{k} tirou {v} no dado.')
	sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('   === Ranking dos Jogadores ===')
for i, v in enumerate(ranking):
	print(f'	{i+1}º lugar: {v[0]} com {v[1]}.')
	sleep(1)