'''
Exercício Python 014: Escreva um programa que converta uma temperatura 
digitando em graus Celsius e converta para graus Fahrenheit.
'''
celsius = float(input('Digite a temperatura em Graus Celsius: '))

fahrenheit = (1.8 * celsius) + 32
print('{}º Celsius equivalem a {:.2f}º Fahrenheit'.format(celsius,fahrenheit))