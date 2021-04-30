class ExpTree:
    def __init__(self,value):   # constructor for tree node
        self.val = value
        self.left = None
        self.right = None


def isOperator(char):
    if (char == "+" or char == "-" or char == "*" or char == "/" or char == "^"):
        return True
    else: return False

def inorder_traversal(treenode):
    if treenode is not None:
        inorder_traversal(treenode.left)
        print(treenode.val),
        inorder_traversal(treenode.right)

def create_tree(expression):
    if expression is None:
         return 0
    stack = []
    for i in expression:
        if not isOperator(i):   #operand, push on stack its node form
            treenode = ExpTree(i)
            stack.append(treenode)

        else:
            # operator; pop latest two operands
            treenode = ExpTree(i)
            node_right = stack.pop()
            node_left = stack.pop()

            # make them children, push them back on stack
            treenode.right = node_right
            treenode.left = node_left

            stack.append(treenode)

    root = stack.pop()

    return root

def evaluate_expression(root):
    if root is None:
        return 0
    # leaf node
    if root.left is None and root.right is None:
        return int(root.val)   # only one node
    # else evaluate the left and right subtree
    left_sum = evaluate_expression(root.left)
    right_sum = evaluate_expression(root.right)

    if root.val == "+":
        return left_sum + right_sum
    if root.val == "-":
        return left_sum - right_sum
    if root.val == "*":
        return left_sum * right_sum
    if root.val == "/":
        return left_sum / right_sum




postfix = "ab+ef*g*-"   #post order traveresed expression
#postfix = "54*10020-+"
regex_tree = create_tree(postfix)
print("the regular expression is ")
inorder_traversal(regex_tree)

#### For evaluating an expression tree
# creating a sample tree, in Preorder fashion
root = ExpTree('+')
root.left = ExpTree('*')
root.left.left = ExpTree('5')
root.left.right = ExpTree('4')
root.right = ExpTree('-')
root.right.left = ExpTree('100')
root.right.right = ExpTree('20')
print(evaluate_expression(root))





