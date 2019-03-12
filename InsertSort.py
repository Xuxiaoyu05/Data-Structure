# 插入排序

# -*- coding: UTF-8 -*-

class Solution:
  def insertSort(self, nums):
  
    length = len(nums)
      
    for i in range(1, length):
      itemToInsert = nums[i]
      position = i
      while position >= 1 and nums[position-1] > itemToInsert:  # 之前的都是排好序的，因此将前面的元素与itemToInsert比较
      	nums[position] = nums[position-1]
		position -= 1
	  nums[position] = itemToInsert
	
     	return nums



nums = [4, 5, 3, 8, 2, 9, 6, 7, 1]

S = Solution()

print(S.insertSort(nums))
