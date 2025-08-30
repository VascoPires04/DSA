class Solution(object):
    def removeDuplicates(self, nums):
        left = 0
        prev = -1000000
        for right in range(len(nums)):
            if nums[right]!=prev:
                prev = nums[right]
                nums[left] = nums[right]
                left+=1
        return left
            
        