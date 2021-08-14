class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        d = []
        cnt = 0
        
        while cnt < len(nums):
            if nums[cnt] in d:
                nums.pop(cnt)
            else:
                d.append(nums[cnt])
                cnt += 1