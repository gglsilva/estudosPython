'''
Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. 
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.
'''
import random

pc = random.randint(0, 11)
tentativas = 0
print('Sou seu computador...')
print('Acabei de pensar em um numero entre 0 e 10, será que consegue adivinhar?')
num = int(input('Qual o seu palpite? '))

while pc != num:
	if num < pc:
		print('Mais... Tente mais uma vez.')
		tentativas += 1
		num = int(input('Qual o seu palpite? '))
	else:
		print('Menos... Tente mais uma vez.')
		tentativas += 1
		num = int(input('Qual o seu palpite? '))
else:
	print('você acertou em {} tentativas, Parabéns'.format(tentativas))

