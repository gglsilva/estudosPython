'''
Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu 
aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o 
aumento é de 15%.
'''

salario = float(input('Digite seu salario mensal: '))

if salario <= 1250.0:
	salario_n = salario + (salario * 0.15 / 100)
else:
	salario_n = salario + (salario * 0.10 / 100)

print('voce recebeu um aumento, seu salario novo é R$ {}'.format(salario_n))