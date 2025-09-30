class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
        int n = profits.length;
        // Min-heap for projects sorted by required capital
        PriorityQueue<int[]> minCapitalHeap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        // Max-heap for profits
        PriorityQueue<int[]> maxProfitHeap = new PriorityQueue<>((a, b) -> b[1] - a[1]);

        for (int i = 0; i < n; i++) {
            minCapitalHeap.offer(new int[]{capital[i], profits[i]});
        }

        int availableCapital = w;
        for (int i = 0; i < k; i++) {
            // Push all affordable projects into maxProfitHeap
            while (!minCapitalHeap.isEmpty() && minCapitalHeap.peek()[0] <= availableCapital) {
                maxProfitHeap.offer(minCapitalHeap.poll());
            }

            if (maxProfitHeap.isEmpty()) break; // No projects can be done

            availableCapital += maxProfitHeap.poll()[1];
        }

        return availableCapital;
    }
}