class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        leftMax, rightMax, water = 0, 0, 0
        while left<right:
            if height[left]<height[right]:
                if height[left]>leftMax:
                    leftMax = height[left]
                else:
                    water+=leftMax - height[left]
                left+=1
            else:
                if height[right]>rightMax:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right-=1
        return water