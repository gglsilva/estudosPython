'''
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo 
será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''
p1 = float(input('Primeiro segmento: '))
p2 = float(input('Segundo segmento: '))
p3 = float(input('Terceiro segmento: '))

if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
	print('Os segmentos acima podem ser um triangulo')
	if p1 == p2 == p3:
		print('Equilátero')
	elif p1 == p2 or p2 == p3 or p3 == p1:
		print('Isósceles')
	else:
		print('Escaleno')
else:
	print('Os segmentos NÃO PODEM formar um triangulo')	