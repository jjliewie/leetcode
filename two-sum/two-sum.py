class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # start = 0
        # end = len(nums)-1
        # while start < end:
        #     if nums[start] + nums[end] == target:
        #         return [start, end]
        #     elif nums[start] + nums[end] > target:
        #         end -= 1
        #     else:
        #         start += 1
        # only if nums is sorted
        
        d = {}
        
        for i in range(len(nums)):
            r = target - nums[i]
            if r in d:
                return i, d[r]
            else:
                d[nums[i]] = i