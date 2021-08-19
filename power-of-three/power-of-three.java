import java.lang.*;

class Solution {
    public boolean isPowerOfThree(int n) {
        
        if(n == 1){
            return true;
        }
        if (n <= 0 || n%3!=0){
            return false;
        }
            
        double a = Math.log10(n)/Math.log10(3);
        int b = (int)a;
        return a==b;
    }
}
