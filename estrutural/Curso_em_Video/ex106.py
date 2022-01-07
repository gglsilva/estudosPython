'''
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e 
o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
'''
c = ('\033[m','\033[0;30;41m','\033[0;30;42m','\033[0;30;44m', '\033[7:30m')

def ajuda(comando):
	titulo(f'Acessando o manual do comando \'{comando}\'', 3)
	print(c[4], end='')
	help(comando)
	print(c[0], end='')


def titulo(msg, cor=0):
	tam = len(msg) + 4
	print(c[cor], end='')
	print('~' * tam)
	print(f'  {msg}')
	print('~' * tam)
	print(c[0], end='')


#Programa principal
comando = ''
while True:
	titulo('SISTEMA DE AJUDA PyHEL', 2)
	comando = str(input("Função ou Biblioteca > "))
	if comando.upper() == 'FIM':
		break
	else:
		ajuda(comando)
titulo('Até Logo!',1)