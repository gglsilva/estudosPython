'''
Exercício Python 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o 
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual 
foi a soma entre elas (desconsiderando o flag).
'''
''' Meu Códigp
cont = 0
soma = 0
while True:
	n = int(input('Digite um numero inteiro: [999 para parar]'))
	if n != 999:
		soma += n		
		cont += 1
	else:
		print(f'A soma dos {cont} valores foi {soma}!')
		break
'''
soma = cont = 0 	#Código Guanabara
while True:
	n = int(input('Digite um numero inteiro: [999 para parar]'))
	if n == 999:
		break
	cont +=1
	soma += num
print(f'A soma dos {cont} valores foi {soma}!')