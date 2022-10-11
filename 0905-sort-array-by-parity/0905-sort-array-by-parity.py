class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even, odd = [], []
        for i in range(len(nums)):
            if nums[i] % 2: 
                odd += [nums[i]]
            else: even += [nums[i]]
        return even + odd