'''
Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de 
artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''
from time import sleep
from random import randint
"""
for i in range(0, 11):
	print(10 - i)
	sleep(0.5)

print('BOW, BOW, BOLL!!!')
"""
for i in range(10, -1, -1):
	print(i)
	sleep(0.5)

print('BUM, BUM, POOW!!!')
