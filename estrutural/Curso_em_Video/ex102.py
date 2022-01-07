'''
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que 
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado 
ou não na tela o processo de cálculo do fatorial.
'''
'''Meu Código
def fatorial(num, show=False):
	c = num
	f = 1
	print('-'*30)
	if show == False:
		while c > 0 :
			f *= c
			c -= 1
		return f
	elif show == True:
		while c > 0 :
			print(f'{c}', end='')
			print(f' x ' if c > 1 else ' = ', end='')
			f *= c
			c -= 1
		return f
print(fatorial(3, show=True))
'''
#Codigo Guanabara
def fatorial(n, show = False):
	"""
	-> Calcula o fatorial de um número.
	:param n: O número a ser calculado.
	:param show: (opcional) Mostrar ou não a conta.
	:retúrn: O valor do Fatorial de um número n.
	"""
	f = 1
	for c in range(n, 0, -1):
		if show:
			print(c, end='')
			if c > 1:
				print(' x ', end='')
			else:
				print(' = ', end='')
		f *= c
	return f


#Programa Principal
print(fatorial(5,show=True))
help(fatorial)
