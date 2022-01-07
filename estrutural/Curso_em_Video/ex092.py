'''
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da 
idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
dados = {'Nome': str(input('Nome: '))}
anoNas = int(input('Ano de Nascimento: '))
idade = date.today().year - anoNas
dados['Idade'] = idade
#'CTPS': int(input('Carteira de Trabalho (0 não tem): '))}
ctps = int(input('Carteira de Trabalho (0 não tem): '))
if ctps != 0:
	dados['CTPS'] = ctps
	dados['A. Contratacao'] = int(input('Ano de Contratação: '))
	dados['Salário: R$'] = float(input('Salário: R$'))
	dados['Aposentadoria'] = dados['Idade']	+ ((dados['A. Contratacao']+35) - date.today().year)
print('-=' * 30)
for k, v in dados.items():
	print(f'	-{k} tem o valor {v}.')
