'''
Exercício Python 017: Faça um programa que leia o comprimento do cateto
oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre 
o comprimento da hipotenusa.
'''
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

h = (co**2 + ca**2) **(1/2)
print('A hipotenusa vai medir {:.2f}'.format(h))
