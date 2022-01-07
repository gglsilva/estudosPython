'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e 
todos os dicionários em uma lista. No final, mostre: 
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''
cadastro = list()
mulhereslist = list()
media = 0
sumIdades = 0
while True:
	dados = dict()
	dados['Nome'] = str(input('Nome: '))
	dados['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
	dados['Idade'] = int(input('Idade: '))
	cadastro.append(dados)
	resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
for i in cadastro:
	for k, v in i.items():
		if k == 'Idade':
			sumIdades += v
media = sumIdades/len(cadastro)
print(cadastro)
print('-=' * 30)
print(f'A) Ao todo temos {len(cadastro)} pessoal(s)')
print(f'B) A media de idade e de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram ', end='')
for p in cadastro:
	if p['Sexo'] == 'F':
		print(f'{p["Nome"]} ', end='')
print()
print(f'D) Lista de pessoas que estão acima da media ',end='')
for p in cadastro:
	if p['Idade'] > media:
		print(f'{p["Nome"]}', end='')
print()
print(' << ENCERROU >>')