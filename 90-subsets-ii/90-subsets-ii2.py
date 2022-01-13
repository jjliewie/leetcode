class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output = [[]]
        if not nums:
            return output
        nums.sort()
        
        for i in nums:
            output += [[i]+j for j in output if [i]+j not in output]
        return output
