# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    ##### Here there is no indicator that shows that one level is over. We are using # to indicate that the left/right/both child are None.
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []

        queue = [root]
        serializeResult = [str(root.val)]

        while (queue):
            node = queue.pop(0)

            for child in [node.left, node.right]:  # check for its children, PUSH them in QUEUE
                if child:  # not none
                    queue.append(child)
                    serializeResult.append(str(child.val))
                else:  # if child is none
                    serializeResult.append("#")

        print(",".join(serializeResult))  # join on commas, because we have -ve valued nodes as well here.
        return ",".join(serializeResult)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        print(data)
        rootNode = TreeNode(int(data[0]))  # not using ord since we have negative numbers here
        currentLevel = [rootNode]
        length = len(data)

        i = 1
        while i < length and currentLevel:
            node = currentLevel.pop(0)  # popped root first
            # check its immediate children
            if data[i] != "#":     # left child check
                child = TreeNode(int(data[i]))
                node.left = child
                currentLevel.append(child)  # pushing into the queue
            i += 1  # move ahead anyways

            if data[i] != "#":   # right child check
                child = TreeNode(int(data[i]))
                node.right = child
                currentLevel.append(child)
            i += 1  # move ahead anyways

        return rootNode

# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(root))