'''
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa 
Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * 2)

print('O IMC dessa pessoa é {}'.format(imc))
if imc >= 18.5 and imc < 25:
	print('Parabéns, você esta na faixa de PESO IDEAL')
elif imc >= 25 and imc < 30:
	print('voce esta com SOBREPESO, cuide-se.')
elif imc >= 30  and imc < 40:
	print('Voce esta OBESO, cuide-se')
elif imc > 40:
	print('você tem obesidade morbida, procure um medico') 

