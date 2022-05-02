class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) > len(num2):
            num2 = (len(num1)-len(num2))*"0"+num2
        else:
            num1 = (len(num2)-len(num1))*"0"+num1
        
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = ""
        over = 0
        for a, b in zip(num1, num2):
            tmp = str(int(a) + int(b) + over)
            over = 0
            if len(tmp) > 1:
                over = int(tmp[0])
            res = tmp[-1] + res
            
        if over != 0:
            res = str(over) + res
        return res