'''
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem 
no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
'''

n1 = float(input('1º Nota: '))
n2 = float(input('2º Nota: '))
media = (n1+n2)/2

if media >= 7:
	print("Tirando {} e {}, a média do aluno é {}".format(n1, n2, media))
	print('O aluno foi APROVADO')
elif media >= 5 and media < 7:
	print("Tirando {} e {}, a média do aluno é {}".format(n1, n2, media))
	print('O aluno esta de RECUPERAÇÃO')
else:
	print("Tirando {} e {}, a média do aluno é {}".format(n1, n2, media))
	print('O aluno foi REPORVADO')

"""
Poderiamos também ter feito as operações logicas da seguinte maneira
7 > media >= 5 --> recuperação
media < 5      --> reprovado
media >= 7	   --> aprovado 
"""