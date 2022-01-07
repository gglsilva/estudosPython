'''
Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas 
pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import date
ano_atual = date.today().year
maior = 0
menor = 0 
for item in range(1, 8):
	ano = int(input('Em que ano a {}º pessoa nasceu? '.format(item)))
	if ano_atual - ano >= 18:
		maior += 1
	else:
		menor += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('É também tivemos {} pessoas menores de idade'.format(menor))