class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        cnt = 0
        for i in arr:
            if i % 2 != 0:
                cnt += 1
            else:
                cnt = 0
            if cnt >= 3:
                return True
        return False