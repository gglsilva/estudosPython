'''
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), 
dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
'''
import moeda as md


#Programa principal
preço = float(input('Digite O Preço: R$ '))
md.aumentar(preço, 0.50)
md.diminuir(preço, 0.50)
md.dobro(preço)
md.metade(preço)