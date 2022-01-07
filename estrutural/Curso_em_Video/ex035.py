'''
Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas 
podem ou não formar um triângulo.
'''

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('terceiro segmento:'))

if (b - c)*(-1) < a < (b + c) and (a - c)*(-1) < b < (a + c) and (a - b)*(-1) < c < (a + b):
	print('Os segmento acima podem formar um triangulo')
else:
	print('Os segmento acima NÃO podem formar um triangulo')