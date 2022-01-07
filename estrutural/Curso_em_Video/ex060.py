l'''
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''
'''meu codigo
num = int(input('Digite um numero para calculamos o seu fatorial: '))
fatorial = 1

for i in range(1, num +1 ):
	fatorial = fatorial * i
	print('Calculando o fatorial de {}!'.format(num,) 

print(fatorial)
'''
num = int(input('Digite um numero para calculamos o seu fatorial: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
	print('{}'.format(c), end='')
	print(' x ' if c > 1 else ' = ', end='')
	f *= c
	c -= 1
print(f, end='')