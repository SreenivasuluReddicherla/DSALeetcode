class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left=0, sum = 0;
        int minLen = Integer.MAX_VALUE;
        int n = nums.length;
        for(int right=0;right<n;right++){
            sum+=nums[right];
            while(sum>=target){
                minLen = Math.min(minLen, right-left+1);
                sum-=nums[left++];
            }
        }
        if(minLen==Integer.MAX_VALUE){
            return 0;
        }else{
            return minLen;
        }

    }
}