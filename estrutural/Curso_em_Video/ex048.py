'''
Exercício Python 048: Faça um programa que calcule a soma entre todos os números INPARES que são múltiplos de três e que se
encontram no intervalo de 1 até 500.
'''
soma = 0
cont = 0
for i in range(1, 501, 2):
	if i % 3 == 0:
		soma += i
		cont += 1

print('A soma de todos os {} valores é {}'.format(cont, soma))
	