'''
Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando 
o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual 
foi a soma entre eles (desconsiderando o flag).
'''
''' meu codigo
soma = 0
cond = True
cont = 0
while cond:
	num = int(input('Digite um numero [999 para parar]: '))
	if num != 999:
		soma += num
		cont += 1
	else:
		print('voce digitou {} e a soma  entre eles foi {}.'.format(cont, soma))
		cond = False
'''
num = cont = soma = 0
while num != 999:
	soma += num
	cont += 1
	num = int(input('Digite um numero [999 para parar]: '))
print('voce digitou {} e a soma  entre eles foi {}.'.format(cont, soma))