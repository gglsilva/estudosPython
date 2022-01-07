'''
Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''
from datetime import date
ano = int(input('Qual ano você quer analisar? Digite 0 para analisar o ano atual: '))

if ano == 0:
	ano = date.today().year
if (ano % 4) == 0:
	if(ano % 100) == 0:
		if (ano % 400) == 0 :
			print('O ano de {} é Bissexto'.format(ano))
		else:
			print('O ano de {} não é Bissexto'.format(ano))
	else:
		print('O ano de {} é Bissexto, tem 366'.format(ano))
else:
	print('O ano de {} não é Bissexto'.format(ano))

'''
if ano % 4 == 0 and ano % 100 != 0 or ano 400 == 0:
	print('o ano {} é bissexto'.format(ano))
else:
	print('o ano {} não é bissexto'.format(ano))
'''
