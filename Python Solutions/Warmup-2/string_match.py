def string_match(a, b):
  count = 0
  for i in range(len(a)):
    if a[i:i+2] == b[i:i+2]:
      count += 1

  if len(a) ==3:
    return count - 1
  
  else:
    return count
