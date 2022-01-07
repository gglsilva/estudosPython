'''
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''
''' meu codigo
def leiaInt(msg):
	while True:
		try:
			valor = int(input(msg))
			break
		except ValueError:
			print('\033[0;mERRO! Digite um valor inteiro válido.\033[m')
	return valor	


def leiaFloat(msg):
	while True:
		try:
			valor = float(input(msg))
			break
		except ValueError:
			print('\033[31mERRO! Digite um valor inteiro válido.\033[m')
	return valor	
'''
def leiaInt(msg):
	while True:
		try:
			n = int(input(msg))
		except (ValueError, TypeError):
			print('\033[31mERRO! Digite um valor inteiro válido.\033[m')
			continue
		except (KeyboardInterrupt):
			print('\033[31mUsario preferiu não digitar esse valor.\033[m')
			return 0
		else:
			return n


def leiaFloat(msg):
	while True:
		try:
			n = float(input(msg))
		except (ValueError, TypeError):
			print('\033[31mERRO! Digite um valor inteiro válido.\033[m')
			continue
		except (KeyboardInterrupt):
			print('\033[31mUsario preferiu não digitar esse valor.\033[m')
			return 0
		else:
			return n


n = leiaInt('Digite um numero Inteiro: ')
f = leiaFloat('Digite um valor Real: ')
print(f'O valor inteiro digitado foi {n} e o valor real foi {f}')