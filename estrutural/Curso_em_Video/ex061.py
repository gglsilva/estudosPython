'''
Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros 
termos da progressão usando a estrutura while.
'''
print(' '*5 + 'Gerador de PA')
print('-='*10)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))

cont = 1

while cont <= 10:
	if cont == 1:
		print(termo, end='-> ')
	else:	
		termo += razao
		print(termo, end='-> ')
	cont += 1

print('FIM!')