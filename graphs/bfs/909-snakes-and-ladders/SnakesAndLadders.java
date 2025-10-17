class Solution {
    public int snakesAndLadders(int[][] board) {
        
        int n = board.length;
        boolean[] visited = new boolean[n * n + 1];
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{1, 0}); // {cell, moves}
        visited[1] = true;

        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int cell = curr[0], moves = curr[1];
            if (cell == n * n) return moves;

            for (int dice = 1; dice <= 6 && cell + dice <= n * n; dice++) {
                int next = cell + dice;
                int[] pos = getPosition(next, n);
                int r = pos[0], c = pos[1];
                if (board[r][c] != -1) next = board[r][c];
                if (!visited[next]) {
                    visited[next] = true;
                    queue.offer(new int[]{next, moves + 1});
                }
            }
        }

        return -1;
    }

    private int[] getPosition(int cell, int n) {
        int r = n - 1 - (cell - 1) / n;
        int c = (cell - 1) % n;
        if ((n - r) % 2 == 0) c = n - 1 - c;
        return new int[]{r, c};
    }
}