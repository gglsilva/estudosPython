'''
Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

num = int(input('Digite um numero qualquer: '))

if (num % 2) != 0:
	print('O numero {} é impar'.format(num))
else:
	print('o numero {} é par'.format(num))
