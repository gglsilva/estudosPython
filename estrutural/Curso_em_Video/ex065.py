'''
Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre 
a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se 
ele quer ou não continuar a digitar valores.
'''
maior = 0
media = 0
menor = 0 
cont = 0
list_n = []
cond = 'Ss'

while True:
	if cond in 'Ss':
		n = int(input('Digite um numero inteiro: '))
		list_n.append(n)
		cond = str(input('Quer continuar? [S/N]'))
		
	elif cond in 'Nn':
		maior = max(list_n)
		menor = min(list_n)
		cont = len(list_n)
		media = sum(list_n)/cont
		print(f'Você Digitou {cont} numeros e a media foi {media}')
		print(f'O maior valor foi {maior} e o menor foi {menor}')
		break
