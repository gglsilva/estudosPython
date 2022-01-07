'''
Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando 
em seguida o primeiro e o último nome separadamente.
'''
nome = str(input('Digite seu nome completo: '))
n = nome.split()

print('seu primeiro nome é {}'.format(n[0]))
print('seu ultimo nome é {}'.format(n[-1]))
