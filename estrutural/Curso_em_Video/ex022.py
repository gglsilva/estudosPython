'''
Exercício Python 022: Crie um programa que leia o nome completo de uma 
pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''
import string as st
nome = str(input('Digite seu nome completo: '))
space = nome.count(' ')
print(space)
#letras = len(nome.split())
print('Maiúsculo: {},\nMinuscula: {},\n'.format(nome.upper(),nome.lower()))
print('Quantidade de letras: {},'.format(len(nome)-space))
print('Quantidade de letras no seu primeiro nome: {}.'.format(len(nome.split(' ')[0])))