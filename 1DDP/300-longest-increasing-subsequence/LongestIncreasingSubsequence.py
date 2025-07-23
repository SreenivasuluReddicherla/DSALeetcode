class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i], dp[j]+1)
        max_len = 0
        for length in dp:
            max_len = max(max_len, length)
        return max_len