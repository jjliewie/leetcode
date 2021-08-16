class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = strs[0]
        strs.pop(0)
        for i in strs:
            cnt = 0
            while cnt < (min(len(result), len(i))):
                if i[cnt] != result[cnt]:
                    result = result[0:cnt]
                cnt += 1
            result = result[0:(min(len(result), len(i)))]
        return result