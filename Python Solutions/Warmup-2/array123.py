def array123(nums):
  for i in range(len(nums)):
    if i < len(nums) - 2:
      if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
        return True
        break 
  else:
    return False
