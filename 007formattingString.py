"""
string, 
integer,
float
bool
"""

nome = 'Vandré'
print(nome, type(nome))

idade = 37
print(idade, type(idade))

altura = 1.76
print(altura, type(altura))

peso = 92
print(peso, type(peso))

imc = peso / (altura**2)

print(f'{nome} tem {idade} anos de idade  e seu imc é: {imc:.2f}')
print('{} tem {} anos de idade  e seu imc é: {:.2f}'.format(nome, idade, imc))