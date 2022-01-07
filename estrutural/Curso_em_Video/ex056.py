'''
Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, 
mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
md_idade = 0
mais_velho = 0
nome_mv = ''
totmulher20 = 0

for i in range(1, 5):
	print('----- {}º PESSOA -----'.format(i))	
	nome = str(input('Nome: '))
	idade = int(input('Idade: '))
	sexo = str(input('Sexo [M/F]: '))
	md_idade += idade
	if i == 1 and sexo in 'Mm':
		mais_velho = idade
		nome_mv = nome
	if sexo in 'Mm' and idade > mais_velho:
		mais_velho = idade
		nome_mv = nome
	if sexo in 'Ff' and idade < 20:
		totmulher20 += 1

print('A media de idade do grupo e de {}'.format((md_idade)/4))
print('O Homem mais velhor tem {} e é o Sr. {}'.format(mais_velho, nome_mv))
print('o Grupo tem {} mulheres com menos de 20 anos'.format(totmulher20))