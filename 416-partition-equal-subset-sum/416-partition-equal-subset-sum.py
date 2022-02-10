class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return False
        if sum(nums) % 2 != 0: return False
        target = sum(nums)//2
        
        use = set([nums[0]])
        for i in nums[1:]:
            temp = list(use)
            for j in temp:
                use.add(i)
                use.add(i+j)
                
        return target in use
        