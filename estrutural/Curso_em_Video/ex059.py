'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
condicao = True



while condicao:
	op = int(input("""[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NUMEROS
[5] SAIR DO PROGRAMA
>>> QUAL É SUA OPÇÃO? """))

	if op == 1:
		soma = num1 + num2
		print('A SOMA ENTRE {} E {} É {}'.format(num1, num2, soma))
		print('=-='*8)
		condicao = False
	elif op == 2:
		multi = num1 * num2 
		print('A MULTIPLICAÇÃO ENTRE {} E {} É {}'.format(num1, num2, multi))
		print('=-='*8)
		condicao = False
	elif op == 3:
		if num1 > num2:
			print('{} é MAIOR que {}'.format(num1, num2))
		elif num2 > num1:
			print('{} é MAIOR que {}'.format(num2, num1))
		else:
			print('Os numeros são IGUAIS')
			print('=-='*8)
		condicao = False
	elif op == 4:
		num1 = int(input('Novo Primeiro valor: '))
		num2 = int(input('Novo Segundo valor: '))
		print('=-='*8)
	elif op == 5:
		print('Fechando Programa... Até breve')
		condicao = False
