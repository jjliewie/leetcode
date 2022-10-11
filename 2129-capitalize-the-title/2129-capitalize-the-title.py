class Solution:
    def capitalizeTitle(self, title: str) -> str:
        k = title.lower().split(" ")
        for i in range(len(k)): 
            if len(k[i]) > 2: k[i] = k[i].capitalize()
        return " ".join(k)
            