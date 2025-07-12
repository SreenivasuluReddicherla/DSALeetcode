class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maxval = 0
        while left < right:
            minval = min(height[left],height[right])
            maxval = max((right-left)*minval, maxval)
            while(left<right and height[left]<= minval):
                left+=1
            while(left<right and height[right]<=minval):
                right-=1
        return maxval