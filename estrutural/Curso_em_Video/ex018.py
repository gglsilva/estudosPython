'''
Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math
angulo = int(input('Digite o valor de um angulo qualquer: '))
print('O ângulo {} tem o SENO de {:.2f}'.format(angulo, math.sin(math.radians(angulo))))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(angulo, math.cos(math.radians(angulo))))
print('O ângulo {} tem o TANGENTE de {:.2f}'.format(angulo, math.tan(math.radians(angulo))))
