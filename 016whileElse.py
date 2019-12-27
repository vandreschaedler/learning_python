count = 1

while count < 100:
  if count % 5 == 0:
    count += 1
    continue
  print(count)
  count = count +1
  break
else:
  print('finished')