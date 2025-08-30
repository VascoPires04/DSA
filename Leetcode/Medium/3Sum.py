class Solution(object):
    def threeSum(self, nums):
        triplets = []
        nums.sort()
        for x in range(len(nums)):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            i = x+1
            f = len(nums)-1
            while i < f:
                soma = nums[x] + nums[i] + nums[f]
                if soma == 0:
                    triplets.append([nums[x], nums[i], nums[f]])
                    f-=1
                    while i < f and nums[f] == nums[f + 1]:
                        f -= 1
                elif soma < 0:
                    i+=1
                else:
                    f-=1
        return triplets
        