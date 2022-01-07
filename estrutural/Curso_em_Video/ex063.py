'''
Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros 
elementos de uma Sequência de Fibonacci. 
'''
print('-' * 40)
n = int(input('Quantos termos você quer mostrar? '))
cont = 3
f1 = 0
f2 = 1
print('{} -> {}'.format(f1, f2), end=' -> ')
while cont <= n:
	fib = f1 + f2
	print(fib, end=' -> ')
	f1 = f2
	f2 = fib
	cont += 1
