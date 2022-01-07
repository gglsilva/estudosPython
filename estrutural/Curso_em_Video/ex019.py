'''
Exercício Python 019: Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos 
alunos e escrevendo na tela o nome do escolhido.
'''
from random import choice
lista = []
for i in range(0,4):
    nome = str(input('digite o nome do {}º aluno: '.format(i+1)))
    lista.append(nome)
aluno = choice(lista)
print(aluno)