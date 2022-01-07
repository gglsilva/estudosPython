'''
Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando
o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''
'''Meu Código
import random

print('=-'*20)
print(' '*7 ,'Vamos jogar Par ou Impar')

v = 0

while True:
	print('=-'*20)
	n = int(input('Diga um valor: '))
	pi = str(input('Par ou Impar? [P/I]'))
	pc = random.randint(0, 10)
	soma = pc + n
	if soma % 2 == 0:
		print('-'*20)
		print(f'você jogou {n} e o computador jogou {pc}. total de {soma} DEU PAR')
		print('-'*20)
		print('você venceu!\nVamos jogar novamente...')
		v += 1
	else:
		print('-'*20)
		print(f'você jogou {n} e o computador jogou {pc}. total de {soma} DEU IMPAR')
		print('-'*20)
		print('você Perdeu!')
		print('=-'*20)
		print(f'Game Over! você venceu {v} vezes')
		break
'''
v = 0
while True:
	jogador = int(input('Diga um valor: '))
	computador = random.randint(0, 10)
	total = jagador + computador
	tipo = ' '
	while tipo not in 'PI':
		tipo = str(input('Par ou Impar?')).strip().upper()[0]
	print(f'Você jogou {jogador} e o computador {computador}. total de {total}')
	print('Deu Par' if total % 2 == 0 else 'Deu Impar')
	if tipo == 'P':
		if total % 2 == 0:
			print('voce venceu!')
			v += 1
		else:
			print('você Perdeu!')
			break
	elif tipo == 'I'
		if total % 2 == 1:
			print('você venceu!')
			v += 1
		else
			print('voce Perdeu!')
			break
	print('Vamos jogar novamente...')
print(f'GAME Over! você venceu {v} vezes.')