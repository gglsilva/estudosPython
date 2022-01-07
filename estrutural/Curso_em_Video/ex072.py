'''
Exercício Python 072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até 
vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''
#meu código
tupla = ('zero','um','dois','três','quatro','cinco',
'seis','sete','oito','nove','dez','onze','doze','treze',
'catorze','quinze','dezesseis','dezessete',
'dezoito','dezenove','vinte')
while True:
	n = int(input('Digite um numero entre 0 e 20: '))
	if n < 0 or n > 20:
		print('Tente novamente. ', end='')
	else:
		print('você digitou o numero {}.'.format(tupla[n]))
	resp = ' '
	while resp not in 'SN':
		resp = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break

'''
#codigo guanabara
tupla = ('zero','um','dois','três','quatro','cinco',
'seis','sete','oito','nove','dez','onze','doze','treze',
'quatorze','catorze','quinze','dezesseis','dezessete',
'dezoito','dezenove','vinte')
while True:
	num = int(input('Digite um numero entre 0 e 20: '))
	if 0 <= num <= 20:
		break
	print('Tente novamente. ', end='')
print(f'Você digitou o numero {tupla[num]}.')
'''