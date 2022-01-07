'''
Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 
10 primeiros termos dessa progressão.
'''
print('='*30)
print(' '*5 + '10 termos de uma PA')
print('='*30)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
'''
print(termo, end=' -> ')
for i in range(0, 9):
	termo += razao
	print(termo, end=' -> ')
print('ACABOU')
'''
decimo = termo + (10 -1) * razao # formula para calcular o 10 termo de uma PA
for i in range(termo, decimo + razao, razao):
	print(' {} '.format(i), end='->')
print(' ACABOU')
