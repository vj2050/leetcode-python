"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    # added init

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        visited = {}
        oldNode = head
        newNode = Node(oldNode.val, None, None)  # val, next, random
        visited[oldNode] = newNode

        def getClonedNode(node):
            if node is not None:
                if node in visited:
                    return visited[node]
                else:  # create new node right away
                    visited[node] = Node(node.val, None, None)
                    return visited[node]
            return None  # when node is none

        # getting clones/copies of the nodes referenced by the random and next pointers
        while oldNode is not None:
            newNode.random = getClonedNode(oldNode.random)
            newNode.next = getClonedNode(oldNode.next)

            # moving 1 step ahead in linked list
            newNode = newNode.next
            oldNode = oldNode.next

        return visited[head]



