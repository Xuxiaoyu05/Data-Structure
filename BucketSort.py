# 桶排序

# -*- coding: UTF-8 -*-

class Solution:
  def bucketSort(self, nums):
    val = max(nums)
    bucket = [0] * (val+1)
    
    for i in nums:
      bucket[i] += 1
    
    res = []
    
    for i in range(len(bucket)):
      if bucket[i] != 0:
        for j in range(bucket[i]):
          res.append(i)
    return res
    
    
nums = [4, 5, 3, 8, 2, 9, 6, 7, 1]

S = Solution()

print(S.bucketSort(nums))
