class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        s = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[s] = nums[s], nums[i]
                s += 1
        """
        Do not return anything, modify nums in-place instead.
        """
        