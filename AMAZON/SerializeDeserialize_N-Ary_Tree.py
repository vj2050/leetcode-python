
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """
        if not root:
            return ""

        queue = [root, None]
        serializeList = []

        while (queue):
            node = queue.pop(0)

            if node == None:
                # end of level
                serializeList.append('#')
                if queue:
                    queue.append(None)

            elif node == 'C':
                serializeList.append('$')

            else:
                serializeList.append(chr(node.val + 48))
                # print("unicode:",chr(node.val + 48))
                if node.children:
                    for child in node.children:
                        queue.append(child)

                if queue[0] != None:
                    queue.append('C')  # marks end of child grp for that parent node

        mystring = "".join(serializeList)
        print(mystring)
        return (mystring)

    def deserialize(self, data: str) -> 'Node':
        if data == "":
            return None

        rootNode = Node(ord(data[0]) - 48, [])
        parentNode = rootNode
        currentLevel, prevLevel = [rootNode], []

        for i in range(1, len(data)):

            if data[i] == '#':
                prevLevel = currentLevel
                currentLevel = []  # fresh

                if prevLevel:
                    parentNode = prevLevel.pop(0)
                else:
                    parentNode = None

            else:
                if data[i] == '$':
                    if prevLevel:
                        parentNode = prevLevel.pop(0)
                    else:
                        parentNode = None
                else:
                    childNode = Node(ord(data[i]) - 48, [])
                    currentLevel.append(childNode)
                    parentNode.children.append(childNode)
        return rootNode

# Your Codec object will be instantiated and called as such:
codec = Codec()
codec.deserialize(codec.serialize([1,None,3,2,4,None,5,6]))