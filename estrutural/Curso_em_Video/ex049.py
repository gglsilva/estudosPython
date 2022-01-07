'''
Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora 
utilizando um laço for.
'''
num = int(input('Digite um numero: '))
print('A TABUADA DE {} é: '.format(num))
for i in range(0,11):
    print('{} x {} = {}'.format(num, i, num*i))
