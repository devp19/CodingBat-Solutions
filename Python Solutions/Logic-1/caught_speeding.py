def caught_speeding(speed, is_birthday):
  
  inc = 5 if is_birthday else 0
  
  if speed <= 60 +inc:
    return 0
  
  elif (61 + inc) <= speed <= (80+inc):
    return 1
  
  else:
    return 2
