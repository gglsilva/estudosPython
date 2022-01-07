'''
Exercício Python 004: Faça um programa que leia algo pelo 
teclado e mostre na tela o seu tipo primitivo e todas as 
informações possíveis sobre ele.
'''
dado = input('Digite algo: ')
print('O tipo primitivo deste valor é: ',type(dado))
print('So tem espaços?',dado.isspace())
print('É um numero?', dado.isnumeric())
print('É alfanumerico', dado.isalnum())
print('É alfabetico?', dado.isalpha())
print('Esta em Maiusculo?', dado.isupper())
print('Esta em minusculo?', dado.islower())
print('Esta capitalizado?', dado.istitle())
