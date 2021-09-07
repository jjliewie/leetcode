class Solution {
    public char slowestKey(int[] releaseTimes, String keysPressed) {
        int cur_sum = 0;
        int max_idx = 0;
        int cur_max = 0;
        
        for(int i = 0; i < releaseTimes.length; i++){
            if (releaseTimes[i]-cur_sum > cur_max){
                cur_max = releaseTimes[i]-cur_sum;
                max_idx = i;
            }
            else if (releaseTimes[i]-cur_sum == cur_max){
                if((int) keysPressed.charAt(i) > (int) keysPressed.charAt(max_idx)){
                    cur_max = releaseTimes[i]-cur_sum;
                    max_idx = i;
                }
            }
            
            cur_sum = releaseTimes[i];
        }
        
        return keysPressed.charAt(max_idx);
    }
}

// same way, just in java
