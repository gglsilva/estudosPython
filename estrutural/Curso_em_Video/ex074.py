'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois 
disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint
'''meu codigo
n1 = random.randint(0,10)
n2 = random.randint(0,10)
n3 = random.randint(0,10)
n4 = random.randint(0,10)
n5 = random.randint(0,10)
numeros = (n1, n2, n3, n4, n5)

# mostre a listagem de números gerados
print(f'Os valores sorteados foram: {numeros}')

#b) menor e o maior valor que estão na tupla
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
'''
'''codigo guanabara
numeros = (randint(1,10), randint(1,10), randint(1,10),
randint(1,10), randint(1,10))
print('Os valores sorteados foram: ',end='')
for n in numeros:
	print(f'{n} ', end='')
print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
'''
from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')
