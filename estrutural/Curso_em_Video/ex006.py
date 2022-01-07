'''
Exercício Python 006: Crie um algoritmo que leia um número 
e mostre o seu dobro, triplo e raiz quadrada.
'''
import math
numero = int(input('Digite um numero: '))
dobro = numero * 2
triplo = numero * 3
raiz = math.sqrt(numero)
print('''O dobro do numero {} é {},
seu triplo é {},
e sua Raiz Quadrada é {}
'''.format(numero, dobro, triplo, raiz))
