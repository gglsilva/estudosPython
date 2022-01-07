def aumentar(preço=0, taxa=0,formato=False):
	res = preço + (preço * taxa/100)
	return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0,formato=False):
	res = preço - (preço*taxa/100)
	return res if formato is False else moeda(res)
	

def dobro(preço=0, formato=False):
	res = preço * 2
	return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
	res = preço/2
	return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
	return f'{moeda}{preço:>8.2f}'.replace('.',',')


def resumo(preço=0, aum=0, dim=0):
	print('_'*30)
	print('\n{:^30}'.format('RESUMO DO VALOR'))
	print('_'*30)
	print('{:<20}{:<10}'.format('Preço analisado:',moeda(preço)))
	print('{:<20}{:<10}'.format('Dobro do Preço:',dobro(preço, True)))
	print('{:<20}{:<10}'.format('Metade do preço:',metade(preço, True)))
	print('{:<2}% {:<16}{:<10}'.format(aum,'de aumento:',aumentar(preço, aum, True)))
	print('{:<2}% {:<16}{:<10}'.format(dim, 'de redução',diminuir(preço, dim, True)))
	print('_'*30)
