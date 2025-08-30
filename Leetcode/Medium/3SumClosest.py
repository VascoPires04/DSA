class Solution(object):
    def threeSumClosest(self, nums, target):
        triplets = []
        nums.sort()
        output = 10000000
        for x in range(len(nums)):
            i = x+1
            f = len(nums)-1
            while i < f:
                soma = nums[x] + nums[i] + nums[f]
                if abs(target-soma) < abs(target-output):output = soma
                if soma == target:
                    return target
                elif soma < target:
                    i+=1
                else:
                    f-=1
        return output
        