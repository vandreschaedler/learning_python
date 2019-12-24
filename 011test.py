number = input('Digite um número: ')

if not number.isdigit():
  print('Não é um inteiro')
elif int(number)%2 == 0: 
  print('É Par!')
else:
  print('É Impar')

print('#########################')

time = input('Digite a hora atual: ')

if int(time[:2]) <= 11: 
  print('Bom dia')
elif int(time[:2]) > 11 and int(time[:2]) <= 17: 
  print('Boa tarde')
else:
  print('Boa Noite')

print('#########################')

name = input('Digite seu nome: ')

if len(name) <= 4:
  print(f'Nome {name} curto')
elif len(name) > 4 and len(name) <=6:
  print(f'Nome {name} normal')
else:
  print(f'Nome {name} longo')