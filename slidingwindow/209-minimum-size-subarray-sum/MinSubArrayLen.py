class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        minLen = float('inf')
        for right in range(len(nums)):
            sum+=nums[right]
            while sum>=target:
                minLen = min(minLen, right-left + 1)
                sum-=nums[left]
                left+=1
        if minLen== float('inf'):
            return 0
        else:
            return minLen