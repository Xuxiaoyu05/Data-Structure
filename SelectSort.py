# 选择排序

# -*- coding:UTF-8 -*-

class Solution:
  def selectSort(self, nums):
    length = len(nums)
    begin = 0
    
    while begin < length - 1:
      min_index = begin
      for i in range(begin, n):
        if nums[i] < nums[min_index]:
          min_index = i
          
      nums[begin], nums[min_index] = nums[min_index], nums[begin]
      begin += 1
    return nums
   
nums = [4, 5, 3, 8, 2, 9, 6, 7, 1]

S = Solution()

print(S.selectSort(nums))    
