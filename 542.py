# Problem link: https://leetcode.com/problems/01-matrix/

from collections import deque

class Solution:
    # checks if the given cell is within the matrix
    def inside(self, rows, cols, r, c):
        return r >= 0 and r < rows and c >= 0 and c < cols
    
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        # final matrix with distances to the nearest zero
        dist = [[-1] * cols for _ in range(rows)]
        
        # list of moves to the neighbouring cells
        moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # start multisource BFS at all zeroes and compute distances
        queue = deque()
        
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                    dist[row][col] = 0
                    
        while queue:
            row, col = queue.popleft()
            for dR, dC in moves:
                newRow = row + dR
                newCol = col + dC
                if self.inside(rows, cols, newRow, newCol) and dist[newRow][newCol] == -1:
                    dist[newRow][newCol] = dist[row][col] + 1
                    queue.append((newRow, newCol))
        
        
        return dist