'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
'''meu codigo
par = ()
msg = ('um', 'outro', 'mais um', 'o último')
numeros = (0,0,0,0)
cont = 0
while True:
	n = int(input(f'Digite {msg[cont]} numero: '))
	numeros = (n,) + numeros[:cont]
	cont +=1
	if cont == 4:
		break
print(f'Você digitou os valores: {numeros[::-1]}')

#A) Quantas vezes apareceu o valor 9.
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
#B) Em que posição foi digitado o primeiro valor 3.
print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
#C) Quais foram os números pares.
print('Os valores pares foram ',end='')
for i in numeros:
	if i % 2 == 0:
		print(i, end=', ')
'''
#codigo guanabara
num = (int(input('Digite um numero: ')),
	int(input('Digite outro numero: '))
	int(input('Digite mais um numero: '))
	int(input('Digite o ultimo numero: ')))
print(f'Você digitou os valores: {num}')
print(f'O valor 9 apareceu {num.count(9)}')
if 3 in num:
	print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
	print('O valor 3 não aparece em nenhuma posição')
print('Os valores pares foram ',end='')
for n in num:
	if n % 2 == 0:
		print(n, end=', ')
		