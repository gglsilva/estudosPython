'''
Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o 
usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''
'''meu código
print('-'*20)
print(' '*5, 'Lojas Super Baratão')
print('-'*20)

totC = contM = totB= 0
produtoB = ' '

while True:
	produto = str(input('Nome do Produto:'))
	preco = float(input('Preço: R$ '))

	#A) qual é o total gasto na compra.
	totC += preco
	#B) quantos produtos custam mais de R$1000.
	if preco >= 1000:
		contM +=1
	#C) qual é o nome do produto mais barato.
	if produtoB == ' ':
		produtoB = produto
		totB = preco
	elif totB > preco:
		produtoB = produto
		totB = preco


	resp = ' '
	while resp not in 'SN':
		resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print('-'*5, 'FIM DO PROGRAMA','-'*5)
print(f'O total da compra foi R$ {totC:.2f}')
print(f'Temos {contM} produto(s) que custa mais de R$ 1000.00.')
print(f'O produto mais barato foi {produtoB} que custa {totB:.2f}')
'''

total = totmil = menor = cont = 0
barato = ' '

while True:
	produto = str(input('Nome do Produto:'))
	preco = float(input('Preço: R$ '))
	cont += 1
	total += preco
	if preco > 1000:
		totmil += 1
	if cont == 1 or preco < menor:
		menor = preco
		barato = produto
	resp = ' '
	while resp not in 'SN':
		resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print('{:-^40}'.format(' FIM DO PREGRAMA '))
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {totmil} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} que custa R$ {menor:.2f}')
