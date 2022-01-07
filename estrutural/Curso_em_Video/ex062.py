'''
Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''
'''meu codigo
print(' '*5 + 'Gerador de PA')
print('-='*10)
termo = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
cont = 1
var_termor = 10
while cont <= var_termor:
	if cont == 1:
		print(termo, end=' -> ')
	else:
		termo += razao
		print(termo, end=' -> ')
	if cont == var_termor:
		print('Pausa!')
		t = int(input('Quantos termos você quer mostrar a mais? '))
		if t  == 0:
			break
		else:
			cont = 1
			var_termor = t
	cont += 1
'''
print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
	total += mais
	while cont <= total:
		print('{} -> '.format(termo), end='')
		termo += razao
		cont += 1
	print('Pausa')
	mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progresão finalizada com {} termos mostrados.'.format(total))


