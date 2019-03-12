# 快速排序

# -*- coding:UTF-8 -*- 

class Solution:
	def quickSort(self, nums, left, right):
		if left < right:
			return
		
		pivot = nums[left]
		i, j = left, right
		
		while i != j:
			while nums[j] >= pivot and j >= left:
				j -= 1
			while nums[i] <= pivot and i <= right :
		    		i += 1
			
			if i < j:
				nums[i], nums[j] = nums[j], nums[i]
		
		nums[left] = nums[i]
		nums[i] = pivot
		
		self.quickSort(nums, left, i-1)
		self.quickSort(nums, i+1, right)


nums = [4, 5, 3, 8, 2, 9, 6, 7, 1]
S = Solution()
print(S.quickSort(nums))
