def combo_string(a, b):
  a_length = len(a)
  b_length = len(b)
  
  if a_length > b_length:
    return b + a + b
  
  else:
    return a + b + a
