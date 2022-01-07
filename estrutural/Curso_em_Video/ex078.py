'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre
 qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
 '''
numeros = []
cont = p = m = 0
while True:
	n = int(input(f'Digite um valor para a posição {cont}: '))
	numeros.append(n)
	cont += 1
	if cont == 5:
		break
print('=-'*20)
print(f'Você digitou os valores {numeros}')
#print(f'O maior valor digitado foi {max(numeros)} na(s) posiçao(ões) {numeros.index(max(numeros))}')
#print(f'O menor valor digitado foi {min(numeros)} na(s) posiçao(ões) {numeros.index(min(numeros))}')
print(f'O maior valor digitado foi {max(numeros)} na(s) posiçao(ões)', end=' ')
for i in numeros:
	if i == max(numeros):
		print(m,end='...')
	m += 1
print(f'\nO menor valor digitado foi {min(numeros)} na(s) posiçao(ões)', end=' ')
for i in numeros:
	if i == min(numeros):
		print(p,end='...')
	p += 1
