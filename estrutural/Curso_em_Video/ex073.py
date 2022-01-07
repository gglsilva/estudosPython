'''
Exercício Python 073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética. 
d) Em que posição está o time da Chapecoense.
'''
times = ('Atlético-MG','Flamengo','Fortaleza EC','Palmeiras',
	'Bragantino','Corinthians','Internacional','Fluminense',
	'Cuiabá','Athletico-PR','Atlético Goianiense','São Paulo',
	'América-MG','Ceará','Santos','Bahia','Juventude','Sport',
	'Grêmio','Chapecoense')
'''meu codigo
#a) Os 5 primeiros times.
print(times[:5])
#b) Os últimos 4 colocados.
print(times[16:])
#c) Times em ordem alfabética. 
ordena_times = []
for item in times:
	ordena_times.append(item)
ordena_times.sort()
for i in ordena_times:
	print(i, end=', ')
#d) Em que posição o time da Chapecoense.
indice_Chapecoense = times.index('Chapecoense')
print(f'O time da Chapecoense esta na {indice_Chapecoense+1}º posição.')
'''
print('-=' *15)
print(f'Lista de times do Brasileirão{times}')
print('-=' *15)
print(f'Os 5 primeiros times são {times[0:5]}')
print('-=' *15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' *15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' *15)
print(f'O Chapecoense está na {times.index("Chapecoense")}')





