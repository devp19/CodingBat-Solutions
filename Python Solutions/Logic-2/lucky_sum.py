def lucky_sum(a, b, c):
  
  l = [a, b, c]
  
  if a!= 13 and b!= 13 and c!= 13:
    return sum(l)
  
  elif a == 13:
    return 0
  
  elif b == 13:
    return a
  
  elif c == 13:
    return a+b
