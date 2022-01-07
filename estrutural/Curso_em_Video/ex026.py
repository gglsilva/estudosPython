'''
Exercício Python 026: Faça um programa que leia uma frase pelo teclado e 
mostre quantas vezes aparece a letra "A", em que posição ela aparece a
primeira vez e em que posição ela aparece a última vez.
'''
frase = str(input('Digite uma frazer qualquer: ')).lower()
cont_a = frase.count('a')
print('A letra "a" aparece {} vezes'.format(cont_a))
print('A primeira letra "a" aparece na posição {}'.format(frase.find('a')+1))
print('A ultima letra "a" aparece na posição {}'.format(frase.rfind('a')+1))