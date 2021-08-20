class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        cnt = 0
        d = []
        for i in sentence:
            if i not in d:
                cnt += 1
                d.append(i)
        return cnt==26