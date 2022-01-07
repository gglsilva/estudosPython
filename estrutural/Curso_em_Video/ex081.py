'''
Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, 
mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
lista = []
cont = 0
while True:
	n = int(input('Digite um valor: '))
	lista.append(n)
	cont += 1
	resp = ' '
	while resp not in 'N':
		resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print('-='*20)
#A) Quantos números foram digitados.
print(f'Foram digitados {cont} valores') # poderia ser len(lista) 
#B) A lista de valores, ordenada de forma decrescente.
orden = sorted(lista) # lista.sort(reverse=True)
print(f'{orden[::-1]}')
#C) Se o valor 5 foi digitado e está ou não na lista.
print('O valor 5 faz parte da lista' if 5 in lista else 'O valor 5 não esta na lista')
