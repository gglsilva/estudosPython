'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie
duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
Ao final, mostre o conteúdo das três listas geradas
'''
numeros = [] 
par = [] 
impar = []
while True:
	#n = int(input('Digite um numero: '))
	#numeros.append(n)
	numeros.append(int(input('Digite um numero: ')))
	if n % 2 == 0:
		par.append(n)
	else:
		impar.append(n)
	resp = ' '
	while resp not in 'SN':
		resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print('Lista com todos os numeros: {}'.format(numeros))
print('Lista com os numeros pares: {}'.format(par))
print('Lista com os numeros impares: {}'.format(impar))
