"""
:s - text
:d - integers
:f - floats
:.(number)f - quantity of decimals
:(CHARACTER)(> OU < OU ^)(QUANTITY)(TYPE -s, d ou f)
"""

num_1 = 1010
num_2 = 3
division = num_1 / num_2

print(division)

print('{:.2f}'.format(division))

print(f'{division:0>10.2f}')

print(f'{division:0>10.2f}')

print(f'{division:0<10.2f}')

print(f'{division:0^10.2f}')

nome = "Vandré Schaedler"

print(nome.lower())
print(nome.upper())
print(nome.title())