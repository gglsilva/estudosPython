'''
Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando 
os espaços.

Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA 
MARATONA.
'''
frase = str(input('Digite uma frazer qualquer:')).replace(" ", "")
frase_invertida = frase[::-1]

print('O inverso de {} é {}'.format(frase, frase_invertida))
if frase == frase_invertida:
	print('Temos um palidromo')
else:
	print('Não temos um palidromo')