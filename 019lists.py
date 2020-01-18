"""
append, insert, pop, del, clear,extend,+,min,max,range
"""

lista1 = [1,2,3,4]

print(lista1)

lista2 = [1,'teste',3,4, 10.5, 'novo']

print(lista2)
print(lista2[1])

print(lista2[::2])

print(lista2[-1])

print(lista2[::-1])

lista1.append('testando')

print(lista1)

l3 = lista1 + lista2

print(l3)

lista1.extend(lista2)

print(lista1)

lista2.insert(2, 'aqui')

print(lista2)

lista2.pop()

print(lista2)

lista2.pop(2)

print(lista2)

l4 = list(range(1,10))

print(l4)

l5 = range(1,10)

for numero in l5:
  print(numero)
