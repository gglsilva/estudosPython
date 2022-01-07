from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
	criarArquivo(arq)


while True:
	resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoas', 'Sair do Sistema'])
	if resposta == 1:
		# Opção de listar o conteúdo de um arquivo!
		lerArquivo(arq)
	elif resposta == 2:
		cabeçalho('Novo Cadastro')
		nome = str(input('Nome: '))	
		idade = leiaInt(input('Idade: '))
		cadastrar(arq, nome, idade)
	elif resposta == 3:
		cabeçalho('Saindo do Sistema...Até Logo.')
		break
	else:
		print('\033[31mERRO! Digite uma opção válida!\033[m')
	sleep(2)	