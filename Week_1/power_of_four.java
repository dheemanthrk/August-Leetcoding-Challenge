class Solution {
    public boolean isPowerOfFour(int num) {    
        return num > 0 && num == Math.pow(4, (int)logn(num, 4)); // return num > 0 && (int)logn(num, 4) == logn(num, 4);
    }
    
    private double logn(int n, int r) { 
        return Math.log(n) / Math.log(r); 
    } 
}