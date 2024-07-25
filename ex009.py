# Faça um programa que leia um número inteiro qualquer
# e mostre na tela a sua tabuada
num = int(input('Digite um número para saber sua tabuada: '))
print('='*30)
print('{:^30}'.format(f'TABUADA DE {num}'))
print('='*30)
for c in range(0,11):
    print(f'{num} x {c} = {c*num}')
