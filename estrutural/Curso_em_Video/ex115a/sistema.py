from lib.interface import *


while True:
	resposta = menu(['Criar Arquivo', 'Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
	if resposta == 1:
		print('opção 1')
	elif resposta == 2:
		print('opção 2')
	elif resposta == 3:
		print('opção 3')	
	elif resposta == 4:
		print('Saindo do Sistema...Até Logo.')
		break
	else:
		print('\033[31mERRO! Digite uma opção válida!\033[m')