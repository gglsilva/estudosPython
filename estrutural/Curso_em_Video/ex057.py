'''
Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
''' Minha solução
sexo = str(input('Informe seu sexo: [M/F] '))
condicao = True

while condicao:
	if sexo in 'MF':
		print('Sexo {} registrado com sucesso'.format(sexo))
		condicao = False
	else:	
		print('Dado inválido. Por favor, Informe seu sexo: ')
		sexo = str(input('Informe seu sexo: [M/F] '))
'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
	sexo = str(input('Dado inválido. Por favor, Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))