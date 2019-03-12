# 选择排序

# -*- coding:UTF-8 -*-

class Solution:
  def selectSort(self, nums):
    length = len(nums) - 1
    
    while length >= 1:
        for i in range(length):
          if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
        length -= 1
     
    return nums
   
nums = [4, 5, 3, 8, 2, 9, 6, 7, 1]

S = Solution()

print(S.selectSort(nums))    
