# Problem link: https://leetcode.com/problems/queens-that-can-attack-the-king/

class Solution:
    def inside(self, x, y) -> bool:
        return x >= 0 and x < 8 and y >= 0 and y < 8
        
        
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        chessboard = [[False] * 8 for _ in range(8)]
        for qX, qY in queens:
            chessboard[qX][qY] = True
        
        # vectors of possible moves
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        ans = []
        
        for deltaX, deltaY in directions:
            x, y = king
            while self.inside(x, y):
                if chessboard[x][y]:
                    ans.append([x, y])
                    break
                x += deltaX
                y += deltaY
        return ans