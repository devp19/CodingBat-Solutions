def centered_average(nums):
  
  smallest = min(nums)
  largest = max(nums)
  
  summ = sum(nums)
  
  return ((summ-smallest-largest) / ((len(nums) - 2)))
