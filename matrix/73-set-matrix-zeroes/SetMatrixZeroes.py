class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix), len(matrix[0])
        # frowzero, fcolzero = False, False
        frowzero = any(matrix[0][j]==0 for j in range(n))
        fcolzero = any(matrix[i][0]==0 for i in range(m))
        # for j in range(n):
        #     if matrix[0][j]==0:
        #         frowzero = True
        # for i in range(m):
        #     if matrix[i][0]==0:
        #         fcolzero = True
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if frowzero:
            for j in range(n):
                matrix[0][j]=0
        if fcolzero:
            for i in range(m):
                matrix[i][0]=0
        """
        Do not return anything, modify matrix in-place instead.
        """
        