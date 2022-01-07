'''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na 
sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''
'''meu codigo
print('_'*35)
print('{:^35}'.format('LISTAGEM DE PREÇOS'))
print('_'*35)
preços = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 
	'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 
	'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 32.90)
cont = 0
for item in preços:
	if cont == 0:
		print(f'{item:.<26}', end='')
		#print(item, end=' ')
		cont += 1
	else:
		print(f'R${item:>7}')
		cont -= 1
print('_'*35)
'''
#Codigo Guanabara
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 
	'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 
	'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 32.90)
print('_'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}'))
print('_'*40)
for pos in range(0, len(listagem)):
	if pos % 2 == 0:
		print(f'{listagem[pos]:.<30}', end='')
	else:
	print(f'R${listagem[pos]:>7.2f}')
print('_'*40) 