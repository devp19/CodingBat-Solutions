def last2(str):
  last2 = str[-2:]
  count = 0
  
  for i in range(len(str)+1):
    if str[i:i+2] == last2:
      count+=1
      
  return count-1
  
