# Faça um programa que leia algo pelo teclado 
# e mostre na tela o seu tipo primitivo 
# e todas as informações possíveis sobre ele
entrada = input('Digite algo: ')
x = type(entrada)
print(f'O tipo da entrada é:{x}')
print('numérico:', entrada.isnumeric())
print('Alpha:', entrada.isalpha())
print('minúsculo:', entrada.islower())
print('Tem espaço:', entrada.isspace())
print(entrada.isalnum())
