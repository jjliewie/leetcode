class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if len(s) < 3:
            return s
        
        if numRows == 1:
            return s
        
        zig = [[] for _ in range(numRows)]
        
        cnt, idx = 0, [0, 0]
        
        while cnt < len(s):
            
            zig[sum(idx)].append(s[cnt])
            
            cnt += 1
            
            idx[0] = sum(idx)
            
            if idx[0] == numRows-1:
                idx[1] = -1
            if idx[0] == 0:
                idx[1] = 1
                
        res = ""
        for i in zig:
            for j in i:
                res += j
        
        return res