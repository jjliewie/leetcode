class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        double = sum(set(nums))*2
        
        return double - sum(nums)