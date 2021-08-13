class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        s = list(set(nums)) + list(set(nums))
        for i in nums:
            s.remove(i)
        return s