class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        triple = sum(set(nums))*3
        
        return int((triple-sum(nums))/2)