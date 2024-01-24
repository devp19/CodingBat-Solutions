def sum67(nums):
  
  found6 = False
  summ = 0
  
  for i in range(len(nums)):
    
    if nums[i] == 6:
      found6 = True
    
    if found6 == True:
      summ+= 0
      
    elif found6 == False:
      summ+= nums[i]
    
    if (nums[i] == 7) and (found6 == True):
      found6 = False
    
  return summ
