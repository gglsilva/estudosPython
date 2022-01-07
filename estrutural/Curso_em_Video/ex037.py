'''
Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário 
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
'''

def converte_b(num):
	binario = ''
	while True:
		binario = binario + str(num % 2)
		num = num // 2
		if num == 0:
			break

	binario = binario[::-1]
	binario = int(binario)
	return binario


def convert_o(num):
	octal = ''
	while True:
		octal = octal + str(num % 8)
		num = num // 8
		if num == 0:
			break
	octal = int(octal[::-1])
	return octal


def convert_h(num):
	hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
	r = []
	hexa = ""
	while num > 0:
		r.append(hex[(num % 16)])
		num = num // 16
	for i in range(len(r)-1,-1,-1):
		hexa = hexa + str(r[i])

	return hexa

num = int(input('Digite um numero inteiro: '))

op = int(input('''Escolha uma base para conversão:
[ 1 ] - converter para binario
[ 2 ] - converter para octal
[ 3 ] - converter para hexadecimal
Sua Opção: '''))

if op == 1:
	print('{} convertido para binario é igual a {}'.format(num, converte_b(num)))
elif op == 2:
	print('{} convertido para octal é igual a {}'.format(num, convert_o(num)))
elif op == 3:
	print('{} convertido para hexadecimal é igual a {}'.format(num, convert_h(num)))
