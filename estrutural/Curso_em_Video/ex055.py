'''
Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o 
menor peso lidos.
'''
''' Minha solução
lista_pessoas = []
for item in range(1, 6):
	peso = float(input('Digite o peso da {}º pessoa: '.format(item)))
	lista_pessoas.append(peso)

print('O maior peso lido foi de {}Kg'.format(max(lista_pessoas)))
print('O menor peso lido foi de {}Kg'.format(min(lista_pessoas)))
'''

maior = 0.0
menor = 0.0

for i in range(1, 6):
	peso = float(input('Peso da {}º pessoa: '.format(i)))
	if i == 1:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		if peso < menor:
			menor = peso


print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))