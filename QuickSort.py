# 快速排序

# -*- coding:UTF-8 -*- 

class Solution:
	def quickSort(self, nums, left, right):
		if left > right:  # 此处别粗心
			return
		
		pivot = nums[left]
		i, j = left, right
		
		while i != j:
			while nums[j] >= pivot and i < j:  # 注意：若j >= i, 则while循环停止，否则会一直交换
				j -= 1
			while nums[i] <= pivot and i < j:
		    		i += 1
			
			if i < j:
				nums[i], nums[j] = nums[j], nums[i]
		
		nums[left] = nums[i]
		nums[i] = pivot
		
		self.quickSort(nums, left, i-1)
		self.quickSort(nums, i+1, right)
		
		return nums


nums = [4, 5, 3, 8, 2, 9, 6, 7, 1]
S = Solution()
print(S.quickSort(nums, 0, len(nums)-1))
