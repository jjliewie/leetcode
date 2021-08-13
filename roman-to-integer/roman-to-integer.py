class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'M' : 1000,
            'CM' : 900,
            'D' : 500,
            'CD' : 400,
            'C' : 100,
            'XC' : 90,
            'L' : 50,
            'XL' : 40,
            'X' : 10,
            'IX' : 9,
            'V' : 5,
            'IV' : 4,
            'I' : 1
        }
        
        result = 0
        
        cnt = 0
        while cnt < len(s):
            for r in roman: 
                if s[cnt:cnt+1] == r:
                    result += roman[r]
                    cnt += 1
                elif s[cnt:cnt+2] == r:
                    result += roman[r]
                    cnt += 2
        print(result)
        
        return result