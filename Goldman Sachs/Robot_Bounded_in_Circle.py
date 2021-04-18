# Input : "GGLLGG" Output : True(Cycle)
class Solution:
    def isRobotBounded(self, instructions):
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # directions elements order  == north, east, south, west   = 0,1,2,3     #clockwise respectively
        direc = 0  # initially facing north
        x = y = 0
        for i in instructions:
            if i == 'R':
                direc = (direc + 1) % 4
            elif i == 'L':
                direc = (direc + 3) % 4  # moving left, i.e negative indices, can write (direc -1)%4 but 1 left = 3 right turns hence + 3
            else:
                # go forward and update x and y and go forward in that direction
                x = x + directions[direc][0]
                y = y + directions[direc][1]
        if (x == 0 and y == 0) or direc != 0:  # if x ,y == 0,0 i.e cycle formed OR direc!=0 i.e after one pass, still not facing north, hence stuck in cycle
            return True

obj = Solution()
print(obj.isRobotBounded("GGLLGG"))





