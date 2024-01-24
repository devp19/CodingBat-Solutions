def lone_sum(a, b, c):
  summ = 0
  
  if a!=b and a!=c:
    summ += a
  
  if b!=a and b!=c:
    summ+= b
  
  if c!=a and c!=b:
    summ+= c
    
  return summ
