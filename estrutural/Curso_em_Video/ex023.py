'''
Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados.
'''
numero = int(input('Informe um numero: '))
uni = numero // 1 % 10
de = numero // 10 %10
ce = numero // 100 % 10
mi = numero // 1000 % 10
print('Analizando o numero: {}'.format(numero))
print('Unidade: {}'.format(uni))
print('Dezemas: {}'.format(de))
print('Centenas: {}'.format(ce))
print('milhar: {}'.format(mi))
