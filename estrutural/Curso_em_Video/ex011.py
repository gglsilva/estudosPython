'''
Exercício Python 011: Faça um programa que leia a largura e a altura 
de uma parede em metros, calcule a sua área e a quantidade de tinta 
necessária para pintá-la, sabendo que cada litro de tinta pinta uma 
área de 2 metros quadrados.
'''
# 1. Quais são os dados de entrada necessários?
#$ largura e altura em metros de uma parede.
# 2. O que devo fazer com estes dados?
#$ calcula a área e a quantidade de tinta necessária para pintá a parede.
# 3. Quais são as restrições deste problema?
#$ devo possuir a lagura e altura para calcular a quantidade de tinta necessaria 
# e quanto ela é capaz de pintar.
# 4. Qual é o resultado esperado?
# uma saida que exiba a área total da parede e a quantidade de necessaria de 
# tinta para pinta-la.
# 5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?

lg = float(input('Digite a largura da parede: '))
al = float(input('Digite a altura da parede: '))

area = lg * al
tinta = area/2
print('A area da parede é {:.2f}m², para essa metragem são necessarios {:.2f}lt de tinta.'.format(area, tinta))
