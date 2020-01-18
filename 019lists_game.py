secret = input('Type a secret word: ')
discovered = []

for item in secret:
  discovered.append('_')
print("".join(discovered))

while True:
  wroteLetter = input('Type a letter: ')

  if wroteLetter in secret:
    for index, item in enumerate(secret):
      if wroteLetter == item:
        discovered.pop(index)
        discovered.insert(index, wroteLetter)
  else:
    print(f'Letter {wroteLetter} does not exist!')

  print("".join(discovered))

  if "".join(discovered) == secret:
    print(f'You Win! The word is {secret}')
    break

    
  