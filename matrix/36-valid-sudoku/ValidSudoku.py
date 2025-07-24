
# Solution 1

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
                if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[(i//3,j//3)]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[(i//3,j//3)].add(board[i][j])
        return True

# Solution 2
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    if(num+"in row"+str(i) in seen or
                        num +"in col"+str(j) in seen or
                        num +"in block"+str(i//3)+"-"+str(j//3) in seen):
                        return False
                seen.add(num+"in row"+str(i))
                seen.add(num +"in col"+str(j))
                seen.add(num +"in block"+str(i//3)+"-"+str(j//3))
        return True