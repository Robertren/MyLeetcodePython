class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        square = [x[:] for x in grid]
        width = len(grid)
        length = len(grid[0])
        for i in range(width):
            for j in range(length):
                if i != 0 and j != 0:
                    square[i][j] = 0
                if i == 0 and j >= 1:
                    square[0][j] = square[0][j-1] + square[0][j]
                if j == 0 and i >= 1:
                    square[i][0] = square[i-1][0] + square[i][0]
        for i in range(width):
            for j in range(length):
                if i != 0 and j != 0:
                    square[i][j] = min(square[i-1][j], square[i][j-1]) + grid[i][j]
        return square[-1][-1]