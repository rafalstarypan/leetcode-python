# Problem link: https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # dimensions of the matrix
        rows = len(mat)
        cols = len(mat[0])
        
        # it is impossible to reshape the matrix
        if rows * cols != r * c:
            return mat
        
        # coordinates of the current cell in the matrix
        curRow = 0
        curCol = 0
        ans = []
        
        for i in range(r):
            newRow = []
            for j in range(c):
                newRow.append(mat[curRow][curCol])
                curCol += 1
                if curCol == cols:
                    curCol = 0
                    curRow += 1
            ans.append(newRow)
        
        return ans