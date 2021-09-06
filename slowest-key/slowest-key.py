class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        cur_sum = 0
        max_idx = 0
        cur_max = 0
        
        for i in range(len(releaseTimes)):
            if(releaseTimes[i]-cur_sum > cur_max):
                cur_max = releaseTimes[i]-cur_sum
                max_idx = i
            elif(releaseTimes[i]-cur_sum == cur_max):
                if(ord(keysPressed[i]) > ord(keysPressed[max_idx])):
                    cur_max = releaseTimes[i]-cur_sum
                    max_idx = i
            cur_sum = releaseTimes[i]
        
        return keysPressed[max_idx]