class Solution:
    
    def factorial(self, num: int) -> int:
        f = 1
        if num >= 1:
            for i in range (1,int(num)+1):
                f = f * i
        return f
        
    def getRow(self, rowIndex: int) -> List[int]:
        result = []
        for i in range(rowIndex+1):
            result.append(int(self.factorial(rowIndex)/(self.factorial(rowIndex-i) * self.factorial(i))))
        return result