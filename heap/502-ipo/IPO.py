class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))  # sort by required capital
        max_profit_heap = []
        i = 0
        n = len(profits)
        available_capital = w

        for _ in range(k):
            # Add all affordable projects into max heap
            while i < n and projects[i][0] <= available_capital:
                heapq.heappush(max_profit_heap, -projects[i][1])  # push profit as negative
                i += 1

            if not max_profit_heap:  # No project affordable
                break

            available_capital += -heapq.heappop(max_profit_heap)

        return available_capital
        