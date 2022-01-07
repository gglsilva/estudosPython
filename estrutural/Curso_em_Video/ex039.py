'''
Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua 
idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo
do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
from datetime import date

ano = int(input('Ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano

print('Quem nasceu em {} tem {} em {}.'.format(ano, idade, ano_atual))
if idade > 18:
	alis = idade - 18
	print('Voce ja deveria ter se alistado a {} anos'.format(alis))
	print('Seu alistamento foi em {}'.format(ano_atual- alis))
elif idade == 18:
	print('Quem nasceu em {} tem/faz 18 anos em {}'.format(ano, ano_atual))
	print('voce deve se alistar imediatamente')
else:
	alis = (idade - 18)*(-1)
	print('Ainda falta {} para o seu alistamento'.format(alis))
	print('Voce deve se alistar em {}'.format(ano_atual+alis))