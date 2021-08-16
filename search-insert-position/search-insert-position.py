class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while start <= end:
            mid = int((start+end)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                start = mid +1
            elif target < nums[mid]:
                end = mid -1
            
        if target < nums[0]:
            return 0
        elif target > nums[len(nums)-1]:
            return len(nums)
        else:
            return start