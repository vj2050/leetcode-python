'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

'''
class Solution:
    def orangesRotting(self, grid):
        # APPROACH : just like BFS ; level order traversing in GRAPH. the levels traversed  == minutes elapsed until no fresh orange remaining.

        queue = []  # to save rotten oranges location only
        freshOranges = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    freshOranges += 1
                elif grid[i][j] == 2:
                    # rotten, save location in queue
                    queue.append((i, j))
        queue.append((-1, -1))  # to mark the end of that level

        # rotting procedure starts
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        minutes = -1  # start with -1 since first rotten orange if already present, then it needs no time to rot.
        while (queue):
            rotX, rotY = queue.pop(0)  # pop first i.e popleft
            if rotX == -1:
                minutes += 1
                # below means reached the end of one level, but still may have its children appended ahead
                if queue:  # still has its children in queue
                    queue.append((-1, -1))  # to mark the end after children
            else:
                for x, y in directions:
                    if 0 <= (rotX + x) < rows and 0 <= (rotY + y) < cols:  # check if still within bounds
                        if grid[rotX + x][rotY + y] == 1:
                            grid[rotX + x][rotY + y] = 2  # if fresh, then rot it
                            freshOranges -= 1
                            queue.append((rotX + x, rotY + y))
        if freshOranges == 0:
            return minutes
        else:
            return -1

obj = Solution()
print(obj.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))