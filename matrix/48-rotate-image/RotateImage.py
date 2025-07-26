class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose the matrix
        for i in range(n):
            for j in range(i,n):
                matrix[i][j], matrix[j][i]=matrix[j][i],matrix[i][j]
        # Reverse the matrix
        for i in range(n):
            left = 0
            right = n-1
            while left<right:
                matrix[i][left],matrix[i][right]=matrix[i][right],matrix[i][left]
                left+=1
                right-=1
        """
        Do not return anything, modify matrix in-place instead.
        """
        