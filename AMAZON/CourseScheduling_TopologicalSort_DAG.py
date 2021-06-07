'''
Topological sort method only works if it is a Directed ACYCLIC graph. In case of cycle, it fails.
'''

from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        stack = []
        visited = [False] * numCourses
        adjList = defaultdict(list)

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
        # print(adjList)
        def helperDFS(node, visited, stack):
            visited[node] = True
            # print("node", node)
            for j in adjList[node]:
                # print("j ",j, node)
                if visited[j] == False:
                    # print("inside if")
                    helperDFS(j, visited, stack)

            stack.append(node)

        for i in range(numCourses):
            if visited[i] == False:
                helperDFS(i, visited, stack)
            # for value in adjList[i]:
        return stack[::-1]

obj = Solution()
print(obj.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))