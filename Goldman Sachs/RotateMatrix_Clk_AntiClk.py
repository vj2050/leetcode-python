class Solution:
    def rotate(self, matrix, clockwise):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        if clockwise:
            matrix[:] = matrix[::-1]
            # print(matrix)

            for i in range(rows):
                for j in range(i, cols):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print("clockwise", matrix)

        elif not clockwise:
        # start from the last element in last row, and keep swapping,
            for i in range(rows - 1, -1, -1):
                for j in range(i, -1, -1):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            # now reverse the matrix to get the original matrix
            matrix[:] = matrix[::-1]
            print("anticlockwise ", matrix)
        return matrix

obj = Solution()
print(obj.rotate([[1,2,3],[4,5,6],[7,8,9]], True))
print(obj.rotate([[7, 4, 1], [8, 5, 2], [9, 6, 3]], False))
