# 冒泡排序

#-*-coding: UTF-8 -*-

class Solution:
	def bubbleSort(self, nums):
		length = len(nums) - 1
		flag = True  # 判断某一轮是否发生交换
		
		while length >= 1 and flag:
			flag = False
			for i in range(length):
				if nums[i] > nums[i+1]:
					nums[i], nums[i+1] = nums[i+1], nums[i]
					flag = True
			length -= 1
		
		return nums
	

nums = [4,5,3,8,2,9,6,7,1]
S = Solution()
print(S.bubbleSort(nums))
