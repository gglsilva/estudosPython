''' meu código
def leiaDinheiro(msg):
	while True:
		valor = input(msg)
		if '.' in valor:
			res = float(valor)
			break
		elif ',' in valor:
			res = float(valor.replace(',','.'))
			break
		elif valor == '':
			print('\033[0;31mERRO! "" é um preço inválido!\033[m')
		elif valor not in '1234567890':
			print(f'\033[0;31mERRO! {valor} é um preço inválido!\033[m')
	return res
'''
#Codigo Guanabara
def leiaDinheiro(msg):
	válido = False
	while not válido:
		entrada = str(input(msg)).replace(',','.').strip()
		if entrada.isalpha() or entrada == '':
			print(f'\033[0;mERRO: \"{entrada}\"é um preço inválido!\033[m')
		else:
			válido = True
			return float(entrada)	