class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curRow, step = 0, 1

        for ch in s:
            rows[curRow] += ch
            if curRow == 0:
                step = 1
            elif curRow == numRows - 1:
                step = -1
            curRow += step

        return "".join(rows)