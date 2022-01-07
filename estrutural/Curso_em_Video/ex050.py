'''
Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que
forem pares. Se o valor digitado for ímpar, desconsidere-o.
'''
cont = 0
soma_pares = 0
for i in range(1, 7):
	item = int(input('Digite o {}º valor: '.format(i)))
	if item % 2 == 0:
		soma_pares += item
		cont += 1
print('Foram digitados {} valores pares'.format(cont))
print('A soma dos valores pares é igual a {}'.format(soma_pares))
