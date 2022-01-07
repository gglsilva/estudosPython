def aumentar(valor, di=0.10):
	porc = valor * di
	aumentar = valor + porc
	print(f'Almentando {int(di*100)}%, temos R$ {aumentar:.2f}')


def diminuir(valor, di=0.10):
	porc = valor * di
	diminuir = valor - porc
	print(f'diminuindo {int(di*100)}%, temos R$ {diminuir:.2f}')


def dobro(valor):
	dobro = valor * 2
	print(f'O dobro de R$ {valor:.2f} é R$ {dobro:.2f}')


def metade(valor):
	metade = valor/2
	print(f'A metade de {valor:.2f} é R$ {metade:.2f}')
