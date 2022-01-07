'''
Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor 
digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''
'''meu código
print('*'*10, ' Tabuada V.3', '*'*10)
num = int(input('Quer ver a Tabuada de qual número: '))

while num > 0:
	cont = 1
	while cont <= 10:
		print('{} X {} = {}'.format(num, cont, num * cont))
		cont += 1
	num = int(input('Quer ver a Tabuada de qual número: '))
print('PROGRAMA TABUADA ENCERRADO, VOLTE SEMPRE!')
'''
#Código Guanabara
while True: 
	n = int(input('Quer Ver a Tabuada de qual valor? '))
	if n < 0:
		break
	print('-' * 30)
	for c in range(1, 11):
		print(f'{n} x {c} = {n*c}')
	print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO, VOLTE SEMPRE!')
