'''
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
'''
matriz = [] # matriz = [[0,0,0], [0,0,0], [0,0,0]]
lista = []
for i in range(3):
	for j in range(3):
		lista.append(int(input(f'Digite um valor para [{i},{j}]'))) #matriz[i][j] = int(input(f'digite um valor para [{i},{j}]'))
	matriz.append(lista[:])
	lista.clear()
print('-='*30)
for m in matriz:
	for l in m:
		print(f'[{l:^5}]', end='')
	print()
