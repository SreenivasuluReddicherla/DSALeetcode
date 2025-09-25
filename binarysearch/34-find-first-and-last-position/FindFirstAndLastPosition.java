class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first = findbounds(nums, target, true);
        int last = findbounds(nums, target, false);
        return new int[]{first, last};
    }
    private int findbounds(int nums[], int target, boolean isFirst){
        int left = 0, right = nums.length-1, bound=-1;
        while(left<=right){
            int mid = left +(right - left)/2;
            if(nums[mid]==target){
                bound = mid;
                if(isFirst){
                    right  = mid-1;
                }else{
                    left = mid +1;
                }
            }else if(nums[mid]>target){
                right = mid-1;
            }else{
                left = mid+1;
            }
        }
        return bound;
    }

}