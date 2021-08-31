class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r = []
        l = 0
        for i in grid:
            l = len(i)
            for j in i:
                r.append(j)
        
        print(len(r))
        
        h = k
        
        if(k > len(r)):
            h = k%len(r)
        
        print(h)
        
        r = r[len(r)-h:] + r[0:len(r)-h]
        
        print(r)
        
        result = []
        cnt = 0
        for i in range(len(grid)):
            a = []
            for j in range(l):
                a.append(r[cnt])
                cnt += 1
            result.append(a)
                
        return result