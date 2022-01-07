'''
Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
'''
num = int(input('Digite um numero: '))
tot = 0
'''
lista_dv = []
lista_nd = []
for i in range(1, num + 1):
	if num % i == 0:
		lista_dv.append(i)
	else:
		lista_nd.append(i)

if len(lista_dv) > 2:
	print('O numero {} foi divisiveis {} vezes'.format(num, len(lista_dv)))
	print('E por isso ele NÃO É PRIMO!')
else:
	print('O numero {} foi divisiveis apenas {} vezes'.format(num, len(lista_dv)))
	print('E por isso ele É PRIMO!')

'''
for c in range(1, num + 1):
	if num % c == 0:
		print('\033[34m', end='')
		tot += 1
	else:
		print('\033[31m', end=' ')
	print('{}'.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(num, tot))
if tot ==2:
	print('É por isso ele É PRIMO!')
else:
	print('É por isso ele NÃO É PRIMO')


