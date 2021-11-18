class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(candi, path, target, res):
            if target < 0:
                return 
            elif target == 0:
                path.sort()
                if path not in res:
                    res.append(path)
                return res
            else:
                for i in range(len(candi)):
                    dfs(candi, path+[candi[i]], target-candi[i], res)
            
        dfs(candidates, [], target, res)

        return res