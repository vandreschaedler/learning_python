texto = 'Python'

for n, letter in enumerate(texto):
  print(n, letter)

for numero in range(20,-1,-5):
  print(numero)

nova = ''

for letra in texto:
  if letra == 't':
    nova += letra.upper()
  elif letra =='h':
    continue
  else:
    nova += letra
print(nova) 