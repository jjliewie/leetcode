class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            d = True
            for k in str(i):
                if int(k) == 0 or i % int(k) != 0:
                    d = False
                    break
            if d: res.append(i)
        return res