class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0
        for i in range(0, len(nums)):
            if i>reachable:
                return False
            reachable = max(reachable, i + nums[i])
        return True