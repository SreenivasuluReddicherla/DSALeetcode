class Solution {
    public int mySqrt(int x) {
        int left = 1, right =x;
        int ans = 0;
        while(left<=right){
            int mid = left + (right-left)/2;
            if((long)mid*mid==x){
                return mid;
            }
            else if((long)mid*mid<x){
                ans = mid;
                left = mid+1;
            }else{
                right = mid-1;
            }
        }
        return ans;
    }
}