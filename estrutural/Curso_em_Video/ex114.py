'''
Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
'''
'''meu codigo
import requests


try:
	response = requests.get('http://pudim.com.br/')
except :
	print('ERRO! site pudim esta indisponivel no momento!')
else:
	print('Consegui acessar o site pudim com sucesso!')
'''
#codigo Guanabara
import urllib.request


try:
	site = urllib.request.urlopen('http://pudim.com.br/')
except urllib.request.URLError:
	print('ERRO! site pudim esta indisponivel no momento!')
else:
	print('Consegui acessar o site pudim com sucesso!')
