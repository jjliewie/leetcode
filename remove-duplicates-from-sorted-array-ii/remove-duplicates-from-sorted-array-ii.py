class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 0
        d = {}
        
        for i in nums:
            d[i] = 0
        
        while cnt < len(nums):
            d[nums[cnt]] += 1
            if d[nums[cnt]] > 2:
                nums.pop(cnt)
            else:
                cnt += 1