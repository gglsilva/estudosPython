'''
Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''
lista_num = []

for i in range(0,3):
	i = int(input('Digite o {}º numero: '.format(i=1)))
	lista_num.append(i)

lista_num.sort()
print('O menor valor é {}'.format(lista_num[0]))
print('O maior valor e {}'.format(lista_num[2]))