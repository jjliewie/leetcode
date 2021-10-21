class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        
        def use(a):  
            if a in seen:
                return False
            else:
                seen.append(a)
            if a == 1:
                return True

            k = 0
            for i in range(len(str(a))):
                k += (int(str(a)[i])**2)
            return use(k)
        
        return use(n)
