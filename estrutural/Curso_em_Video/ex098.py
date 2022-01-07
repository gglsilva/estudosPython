'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, 
fim e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
"""meu codigo
from time import sleep

def contador(i, f, p):
	print('-='*20)
	print(f'Contagem de {i} até {f} de {p} em {p}' if p > 0 else f'Contagem de {i} até {f} de {p*(-1)} em {p*(-1)}')
	if i < f and p > 0:
		for i in range(i, f+1, p):
			print(f'{i} ', end='')
			#sleep(1)
		print('FIM!')
	elif i > f and p < 0:
		for i in range(i, f-1, p):
			print(f'{i} ', end='')
			#sleep(1)
		print('FIM!')
	elif i > f and p > 0:
		for i in range(i, f-1, -p):
			print(f'{i} ', end='')
			#sleep(1)
		print('FIM!')


contador(1,10, 1)
contador(10, 0, -2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
"""
#código Guanabara
from time import sleep
def contador(i,f, p):
	if p < 0:
		p *= -1
	if p == 0:
		p =1
	print('-='*20)
	print(f'Contagem de {i} ate {f} de {p} em {p}')
	sleep(2.5)
	if i < f:
		cont = i
		while cont <=f:
			print(f'{cont} ',end='', flush=True)
			sleep(0.5)
			cont += p
		print('Fim!')
	else:
		cont = i
		while cont >= f:
			print(f'{cont} ',end='', flush=True)
			sleep(0.5)
			cont -= p
		print('Fim!')


#Programa principal
contador(1, 10, 1)
contador(10,0,2)
print('-='*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('fim: '))
pas=int(input('passo:' ))
contador(ini,fim, pas)
