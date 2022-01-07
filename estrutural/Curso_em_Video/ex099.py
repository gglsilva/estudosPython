'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
'''meu codigo
from time import sleep
def maior(*num):
	print('-='*25)
	print('Analisando os valores passados...')
	if len(num) != 0:
		for i in num:
			print(f'{i} ', end='', flush=True)
			sleep(0.5)
		print(f'Foram informados {len(num)} valores ao todo.')
		sleep(0.5)
		print(f'O maior valor informado foi {max(num)}')
	else:
		print('Foram informados 0 valores ao todo.')


maior(1,3,5,6,9)
maior(2)
maior(5,3)
maior(4,6,1,8,20,12,45,67,46)
maior()
'''
from time import sleep


def maior(* num):
	cont = maior = 0
	print('-=' * 30)
	print('Analisando os valores passados...')
	for valor in num:
		print(f'{valor}', end='', flush=True)
		sleep(0.3)
		if cont == 0:
			maior = valor
		else:
			if valor > maior:
				maior = valor
		cont += 1
	print(f'Foram informados {cont} valores ao todo.')
	print(f'O maior valor informado foi {maior}')
maior(1,3,5,6,9)
maior(2)
maior(5,3)
maior(4,6,1,8,20,12,45,67,46)
maior()