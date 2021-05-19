class Solution:
    def getMaximumGold(self, grid):
        # [[False for i in range(len(cols))] for j in range(len(rows))]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        maxGold = float("-inf")

        def helperDFS(i, j, visited, grid):

            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):  # out of bounds
                return 0

            if grid[i][j] == 0:
                visited[i][j] = True
                return 0

            if visited[i][j] == True:
                return 0

            else:
                # have some gold at that position + position within bounds
                visited[i][j] = True

                maxVal = grid[i][j] + max(helperDFS(i - 1, j, visited, grid),  # UP
                                          helperDFS(i + 1, j, visited, grid),  # DOWN
                                          helperDFS(i, j - 1, visited, grid),
                                          helperDFS(i, j + 1, visited, grid))
                visited[i][j] = False
                return maxVal

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxGold = max(maxGold, helperDFS(i, j, visited, grid))

        return maxGold
        print(visited)

obj = Solution()
print(obj.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))