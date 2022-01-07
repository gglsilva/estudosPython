'''
Exercício Python 008: Escreva um programa que leia um valor em metros e o 
exiba convertido em centímetros e milímetros.
'''
metros = float(input('Digite um valor em metros: '))
cm = metros * 100
mm = metros * 1000

print('{} metros equivalem há:{} cm e {} mm.'.format(metros, cm, mm))
