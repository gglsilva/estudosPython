'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, 
só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
'''
'''Meu Programa
def leiaInt(num):
	while True:
		numero = input(num)
		if numero.isnumeric():
			return int(numero)
			break
		else:
			print('ERRO! Digite um numero inteiro valido.')


#Programa principal
n = leiaInt('Digite um numero inteiro: ')
print(f'voce acabou de digitar o numero {n}.')
'''
def leiaInt(msg):
	ok = False
	valor = 0 
	while True:
		n = str(input(msg))
		if n.isnumeric():
			valor = int(n)
			ok = True
		else:
			print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
		if ok:
		break
	return valor


n = leiaInt('Digite um numero: ')	
print(f'voce acabou de digitar o numero {n}.')
