class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dictionary = {}
        p_list = [word for word in pattern]
        s_list = s.split(" ")
        
        if len(p_list) != len(s_list):
            return False
        
        seen = []
        
        for a, b in zip(p_list, s_list):
            if a in dictionary.keys():
                if dictionary[a] != b:
                    return False
            else:
                if b not in seen:
                    dictionary[a] = b
                    seen.append(b)
                else:
                    return False
        return True