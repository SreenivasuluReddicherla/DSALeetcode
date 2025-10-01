class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        result = []

        # Initialize with first element of nums2 for each nums1[i]
        for i in range(min(len(nums1), k)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while k > 0 and heap:
            s, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            k -= 1

            # If possible, move to next element in nums2
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result
        