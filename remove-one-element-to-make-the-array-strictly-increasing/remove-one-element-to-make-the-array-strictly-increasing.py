class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if nums == sorted(nums) and len(nums) == len(set(nums)):
            return True
        for i in range(len(nums)):
            k = copy.copy(nums)
            k.pop(i)
            if k == sorted(k) and len(k) == len(set(k)):
                return True
        return False