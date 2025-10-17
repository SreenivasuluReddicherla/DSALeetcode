class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coordinates(square):
            r, c = divmod(square - 1, n)
            row = n - 1 - r
            col = c if r % 2 == 0 else n - 1 - c
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (square, moves)

        while queue:
            square, moves = queue.popleft()
            if square == n * n:
                return moves
            for roll in range(1, 7):
                next_square = square + roll
                if next_square > n * n:
                    break
                r, c = get_coordinates(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))
        return -1

        