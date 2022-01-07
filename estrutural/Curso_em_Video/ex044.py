'''
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço 
normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''
print('='*10 + 'Lojas Guanabara' + '='*10)

valor = float(input('Preço das compras: R$'))
op = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/pix
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))
if op == 1:
	pagar = valor - (valor * 0.10)
	print('voce ganhou um desconto de 10%')
	print('O valor a pagar ficou em R$ {}'.format(pagar))
elif op == 2:
	pagar = valor - (valor * 0.05)
	print('voce ganhou um desconto de 5%')
	print('O valor a pagar ficou em R$ {}'.format(pagar))
elif op == 3:
	parcelas = valor / 2
	print('Sua compra será parcelada em 2x de R$ {} sem juros'.format(parcelas))
	print('O valor a pagar ficou em R$ {}'.format(valor))
elif op == 4:
	parcelas = int(input('Quantas parcelas? '))
	pagar = valor + (valor * 0.20)
	v_parcelas = pagar / parcelas
	print('Sua compra será parcelada em {}x de R${} com juros'.format(parcelas, v_parcelas))
	print('O valor a pagar ficou em R$ {}'.format(pagar))