'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
'''
'''Meu codigo
dic = {}
nome = str(input('Nome: '))
media = float(input(f'Media de {nome}: '))
situação = ''
if media < 6:
	situação = 'REPROVADO'
elif 6 > media < 7:
	situação = 'RECUPERAÇÃO'
elif media >= 7:
	situação = 'APROVADO'
dic['Nome'] = nome
dic['Média'] = media
dic['Situação'] = situação
print('-='*35)
print('- Nome é igual a {}'.format(dic['Nome']))
print('- Média é igual a {}'.format(dic['Média']))
print('- Situação é igual a {}'.format(dic['Situação']))
'''
aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
	aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
	aluno['situação'] = 'Recuperação'
else:
	aluno['situação'] = 'Reprovado'
print('-=' * 30)
for k, v in aluno.items():
	print(f'  - {k} é igual a {v}')


