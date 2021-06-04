from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjList = defaultdict(list)
        visited = {}

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
        print("adjacency list ", adjList)

        def isCycle(node, tracker, visited):
            tracker[node] = True  # visited
            visited[node] = True
            for i in adjList[node]:
                if i not in visited and isCycle(i, tracker, visited):
                    # cycle
                    return True
                elif i in tracker:
                    # cycle detected
                    return True

            tracker.pop(node)
            return False

        for i in range(numCourses):
            tracker = {}
            if isCycle(i, tracker, visited):
                return False
        return True

obj = Solution()
print(obj.canFinish(2,[[1,0],[0,1]]))