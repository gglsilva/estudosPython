'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
'''
'''meu codigo
cadastro = list()
gols = []
maxgols = 0
while True:
	dados = dict()
	dados['Nome'] = str(input('Nome: '))
	part = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
	for i in range(1, part + 1):
		gols.append(int(input(f'Quantos gols na partida {i}? ')))
	dados['Gols'] = gols[:]
	dados['Total'] = sum(gols)
	if sum(gols) > maxgols:
		maxgols = sum(gols)
	cadastro.append(dados)
	gols.clear()
	resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
	if resp == 'N':
		break
print(cadastro)
print('-=' * 30)
print('{:^5}{:<15}{:<15}{:<5}'.format('Cod', 'Nome', 'Gols', 'Total'))
print('_'*40)
cod = 0
for i in cadastro:
	if i['Total'] == maxgols:
		
		
print(maxgols)
'''
time = list()
jogador = dict()
partidas = list()
while True:
	jogador.clear()
	jogador['nome']=str(input('nome do jogador: '))
	tot=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
	partidas.clear()
	for c in range(0, tot):
		partidas.append(int(input(f'	Quantos gols na partida {c} marcou? ')))
	jogador['gols'] = partidas[:]
	jogador['Total'] = sum(partidas)
	time.append(jogador.copy())
	while True:
		resp = str(input('Quer continuar? [S/N] ')).upper()[0]
		if resp in 'SN':
			break
		print('ERRO! Responda apenas S ou N.')
	if resp == 'N':
		break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
	print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
	print(f'{k:>3}', end='')
	for d in v.values():
		print(f'{str(d):<15}',end='')
	print()
print('_' * 40)
while True:
	busca = int(input('Mostra dados de qual jogador? (999 para parar)	'))
	if busca == 999:
		break
	if busca >= len(time):
		print(f'ERRO! Não existe jogador com codigo de {busca}!')
	else:
		print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
		for i, g in enumerate(time[busca]['gols']):
			print(f'	No jogo {i+1} fez {g} gols.')
	print('_' * 40)
print('<< VOLTE SEMPRE >>')
