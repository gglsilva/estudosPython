'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e 
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, 
incluindo o total de gols feitos durante o campeonato.
'''
dados = {
	'Nome': str(input('Nome: ')),
	}
gols = []
qtPartidas = int(input(f'Quantas partidas {dados["Nome"]} jogou: '))
for i in range(1, qtPartidas+1):
	gols.append(int(input(f'Quantos gols na partida {i}? ')))
dados['Gols'] = gols
dados['Total'] = sum(gols)
print('-=' * 30)
print(dados)
print('-=' * 30)
for k, v in dados.items():
	print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["Nome"]} jogou {len(gols)} partidas.')
cont = 1
for i in dados["Gols"]:
	print(f'	=> Na partida {cont}, fez {i} gols.')
print(f'foi um Total de {dados["Total"]}.')
'''cod Guanabara
jogador = dict()
partidas = list()
jogador['nome']=str(input('nome do jogador: '))
tot=int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, tot):
	partidas.append(int(f'	Quantos gols na partida {c} marcou? '))
jogador['Total'] = sum(partidas)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
	print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'o jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
	print(f'	=>Na partida {i},fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
'''