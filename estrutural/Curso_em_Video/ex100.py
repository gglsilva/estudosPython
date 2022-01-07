'''
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira 
função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares 
sorteados pela função anterior.
'''
from random import randint
from time import sleep

'''meu código
def sorteia():
	lista = []
	print('Sorteando 5 valores da lista: ', end='')
	for i in range(1, 6):
		n = randint(1, 10)
		if n not in lista:
			print(f'{n} ', end='', flush=True)
			sleep(1)
			lista.append(n)
		else:
			while True:
				n = randint(1, 10)
				if n not in lista:
					print(f'{n} ', end='', flush=True)
					sleep(1)
					lista.append(n)
					break
	print('PRONTO!')
	return lista


def somaPar(num):
	soma = 0
	print(f'Somando os valore pares de {num}, temos ', end='')
	for i in num:
		if i % 2 == 0:
			soma += i
	print(f'{soma}')


numeros = sorteia()
somaPar(numeros)
'''
#Código Guanabara
def sorteia(lista):
	print('Sorteando 5 valores da lista: ',end='')
	for cont in range(0,5):
		n=randint(1,10)
		lista.append(n)
		print(f'{n}', end='', flush=True)
		sleep(0.3)
	print('PRONTO!')


def somaPar(lista):
	soma = 0
	for valor in lista:
		if valor %2 == 0:
			soma += valor
	print(f'Somando os valores pares de {lista}, temos {soma}.')

números = list()
sorteia(números)
somaPar(numeros)