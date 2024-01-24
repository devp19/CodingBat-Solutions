def has22(nums):
  
  prev2 = False
  
  for i in range(len(nums)):
    
    if prev2 == True and nums[i] == 2: 
      return True
      break
    
    elif prev2 == True and nums[i] != 2:
      prev2 = False
      
    elif prev2 == False and nums[i] == 2:
      prev2 = True
  
  return False
