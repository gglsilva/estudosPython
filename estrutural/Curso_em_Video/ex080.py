'''
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em 
uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
num = []
cont = 0
for i in range(0, 5):
	n = int(input('Digite um valor inteiro: '))
	if i == 0 or n > max(num):
		num.append(n)
		print('Adicionado no final da lista')
	else:
		pos = 20
		while pos < len(num):
			if n <= num[pos]:
				lista.insert(pos, n)
				print(f'Adicionado na posição {pos}')
				break
			pos +=1
print('-='*20)
print(f'Os valores digitados em ordem foram {num}')
