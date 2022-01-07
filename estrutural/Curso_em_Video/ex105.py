'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar 
um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''
def notas(* notas, sit=False):
	"""
	-> Função para analisar notas e situações de vários alunos.
	:param n: uma ou mais notas dos alunos(aceita varias)
	:param sit: valor opcional, indicando se deve ou não adicionar a situação
	:return: dicionário com várias informações sobre a situação da turna.
	"""
	dados = dict()
	dados['Total'] = len(notas)
	dados['Maior'] = max(notas)
	dados['Menor'] = min(notas)
	dados['Media'] = sum(notas)/len(notas)
	if sit == True:
		if dados['Media'] < 5:
			dados['Situação'] = 'Ruim'
		elif dados['Media'] >= 5 and dados['Media'] < 7:
		 	dados['Situação'] = 'Razoável'
		else:
			dados['Situação'] = 'Boa'
	return dados


#Programa principal
resp = notas(6.2, 7.5, 10.0, 6.5)
print(resp)
