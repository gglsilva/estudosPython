'''
Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga 
mostrar os números como um valor monetário formatado.
'''
import moeda


valor = float(input('Digite um valor: '))
metade = moeda.metade(valor)
m = moeda.moeda(metade)
print(f'A metade de {moeda.moeda(valor)} é {m}')