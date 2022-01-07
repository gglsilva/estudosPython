'''
Exercício Python 013: Faça um algoritmo que leia o salário de um 
funcionário e mostre seu novo salário, com 15% de aumento.
'''
salario = float(input('Digite seu salario do mês: '))

aumento = salario * 0.15
salario_novo = salario + aumento
print('''Seu salario é R$ {}, você receberá R$ {} equivalente a 15% de aumento,
no total receberar R$ {} '''.format(salario,aumento,salario_novo))