'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha
'''
matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = 0
for i in range(3):
	for j in range(3):
		matriz[i][j] = int(input(f'digite um valor para [{i},{j}]'))
print('-='*30)
for m in matriz:
	for l in m:
		print(f'[{l:^5}]', end='')
		soma += l
	print()
print(f'Soma de todos os valores {soma}')
terceira = matriz[0][2] + matriz[1][2] + matriz[2][2]
segunda = [matriz[0][1],matriz[1][1], matriz[2][1]]
print(terceira)
print(max(segunda))
