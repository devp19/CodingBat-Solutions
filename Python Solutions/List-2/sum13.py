def sum13(nums):
  summ = 0
  index_before = False
  
  for i in range(len(nums)):
    
    if nums[i] == 13:
      summ+= 0
      index_before = True
    
    elif (nums[i] != 13) and (index_before == False): 
      summ += nums[i]
    
    elif (nums[i] != 13) and (index_before == True):
      summ += 0
      index_before = False
      
  return summ
