'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar 
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista
composta.
'''
from random import randint
print('_'*30,'\n')
print('{:^30}'.format('Joga na Mega Sena'))
print('_'*30)
jogos = []
cont = 0
j = int(input('Quantos jogos voce quer que eu sorteie? '))
while cont < j:
	for i in range(1,7):
		n = randint(1,60)
		if n not in jogos:
			jogos.append(n)
		else:
			n=randint(1,60)
			jogos.append(n)
	cont += 1
	jogos = sorted(jogos)
	print(f'Jogo {cont}:',jogos)
	jogos.clear()