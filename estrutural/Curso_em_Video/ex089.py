'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno 
individualmente.
'''
dados = []
aluno = []
while True:
	aluno.append(str(input('Nome: ')))
	aluno.append(float(input('Nota 1: ')))
	aluno.append(float(input('Nota 2: ')))
	media = (aluno[1] + aluno[2])/2
	aluno.append(media)
	dados.append(aluno[:])
	aluno.clear()
	resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	if resp in 'Nn':
		break
print('-='*20)
print('{:^5}{:<15}{:<5}'.format('No.', 'Nome', 'Média'))
print('_'*30)
for a in dados:
	print(f'{dados.index(a):^5}', end='')
	for j in range(0, len(a), 3):
		print(f'{a[j]:<15}', end='')
	print()
print('_'*30)

while True:
	al = int(input('Mostra as notas de qual aluno? (999 interrompe): '))
	if al == 999:
		break
	else:
		print(f'Notas de {dados[al][0]} são [{dados[al][1]}, {dados[al][2]}]',)
