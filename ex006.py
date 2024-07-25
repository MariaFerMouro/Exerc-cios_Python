# Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:
import math
x = float(input('Digite um número: '))
y = x**(1/2)
#print(f'A raíz quadrada de {x} é {math.sqrt(x)}')
print('{:.2f}'.format(y))
