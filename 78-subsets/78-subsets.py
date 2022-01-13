class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        
        for i in nums:
            output += [[i]+j for j in output]
        
        return output