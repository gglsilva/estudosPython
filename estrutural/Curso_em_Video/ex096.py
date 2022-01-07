'''
Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.
'''
def area(l, c):
	print(f'A área de um terreno {l} x {c} é igual a {l*c}m²')


#Programa principal
print(' Controle de Terrenos')
print('-'*23)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)