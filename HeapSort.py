# 堆排序

# -*- coding:UTF-8 -*-

class Solution:  
  def heapify(self, nums, root, heapsize):
    # 堆调整
    left = 2 * root
    right = 2* root + 1
    larger = root
    if left < heapsize and nums[left] > nums[larger]:  # 注意：此处应该先判断left < heapsize，否则若left越界，nums[left]会报错
      larger = left
    if right < heapsize and nums[right] > nums[larger]:
      larger = right
    
    if larger != root:
      nums[larger], nums[root] = nums[root], nums[larger]
      self.heapify(nums, larger, heapsize)
    
   
  def buildMaxHeap(self, nums):
    # 构建初始大根堆
    heapsize = len(nums) 
    for i in range(heapsize//2-1, -1, -1):  #从最后一个非叶子结点进行堆调整
      self.heapify(nums, i, heapsize)
    
    
  def heapSort(self, nums):
    # 构建初始最大堆
    self.buildMaxHeap(nums) 
    # 堆排序
    heapsize = len(nums) - 1
    for i in range(heapsize, 0, -1):
      nums[0], nums[i] = nums[i], nums[0]
      self.heapify(nums, 0, i)  # 从上到下进行堆调整
      
    return nums     # nums从小到大
#     return nums[::-1]   # nums从大到小

nums = [4, 5, 3, 8, 2, 9, 6, 7, 1]

S = Solution()

print(S.heapSort(nums))
