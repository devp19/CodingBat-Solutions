def close_far(a, b, c):
  if ((0 <= abs(a - b) <= 1 ) and ((abs(a-c)) >= 2) and (abs(c-b) >= 2)):
      return True
  elif (0 <= (abs(a - c) <= 1) and ((abs(a-b)) >= 2) and (abs(c-b) >= 2)):
      return True
  else:
      return False
