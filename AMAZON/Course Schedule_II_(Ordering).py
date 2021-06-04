from collections import defaultdict
class Solution(object):
    WHITE = 1       # not visited
    GRAY = 2        # in process
    BLACK = 3       # already visited, done

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        stack = []
        # visited = [False]*numCourses
        is_possible = True
        adjList = defaultdict(list)

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
        print(adjList)
        # by default all vertices are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}

        def helperDFS(node):
            nonlocal is_possible

            # if cycle found , dont recurse further
            if not is_possible:
                return
            # else, start recursion
            color[node] = Solution.GRAY  # PICKED

            # Traversing on neighbouring vertices

            # visited[node] = True
            # print("node", node)
            if node in adjList:
                for j in adjList[node]:
                    # print("j ",j, node)
                    # if visited[j] == False:
                    if color[j] == Solution.WHITE:  # i.e if unvisited
                        helperDFS(j)

                    elif color[j] == Solution.GRAY:
                        # already visited, detects cycle
                        is_possible = False
            # recusrion ends here : Mark it as black (done)
            color[node] = Solution.BLACK
            stack.append(node)

        for i in range(numCourses):
            # if node is fresh, unprocessed, call dfs func
            if color[i] == Solution.WHITE:
                # if visited[i] == False:
                helperDFS(i)
            # for value in adjList[i]:
        return stack[::-1] if is_possible else []


obj = Solution()
print(obj.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))