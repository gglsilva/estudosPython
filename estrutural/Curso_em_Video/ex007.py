'''
Exercício Python 007: Desenvolva um programa que leia as duas notas de um 
aluno, calcule e mostre a sua média.
'''
n1 = int(input('Digite a primeira nota do Aluno: '))
n2 = int(input('Digite a segunda nota do Aluno: '))
media = (n1+n2)/2
print('A media entre {} e {} é {}'.format(n1, n2, media))
