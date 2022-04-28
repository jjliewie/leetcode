class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        k, temp = 0, 1
        while k < num:
            k += temp
            temp += 2
        return k == num