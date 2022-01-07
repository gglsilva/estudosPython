'''
Exercício Python 024: Crie um programa que leia o nome de uma cidade diga 
se ela começa ou não com o nome "SANTO".
'''

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('o nome da cidade tem santo? {}'.format('santo' in cidade.lower()))