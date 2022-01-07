'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha 
separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''
princ = []
par = []
impar = []
for i in range(1, 8):
	n = int(input(f'Digite O {i}º valor: '))
	if n % 2 == 0:
		par.append(n)
	else:
		impar.append(n)
	par.sort()
	impar.sort()
#print(par, impar)
princ.append(par[:])
princ.append(impar[:])
par.clear()
impar.clear()
print(f'Os valores pares digitados foram {princ[0]}')
print(f'Os valores impares digitados foram {princ[1]}')

'''
num = [[],[]]
valor = 0
for i in range(1, 8):
	valor = int(input(f'Digite O {i}º valor:'))
	if valor % 2 == 0:
		num[0].append(valor)
	else:
		num[1].append(valor)
print('-='*30)
print(f'Os valores pares digitados foram {princ[0].sort()}')
print(f'Os valores impares digitados foram {princ[1].sort()}')
'''