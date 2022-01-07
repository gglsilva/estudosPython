'''
Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem
de apresentação de trabalhos dos alunos. Faça um programa que leia o nome 
dos quatro alunos e mostre a ordem sorteada.
'''
from random import choice
from random import shuffle #reorganiza a ordem dos itens de uma lista por exemplo
'''
Poderia ter apenas utilizado o metodo shuffle da biblioteca random, mas preferir 
resolver o problema usando logica ;)
'''
lista = []
lista_t =[]
for i in range(0,4):
    nome = str(input('digite o nome do {}º aluno'.format(i+1)))
    lista.append(nome)
print('Ordem de apresentações dos trabalhos: ')

for i in range(0,4):
    if nome in lista_t:
        nome = choice(lista)
        lista_t.append(nome)
    else:
        nome = choice(lista)
        lista_t.append(nome)
print(lista_t)