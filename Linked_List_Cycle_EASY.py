def detectCycle(self, head):
    visited_node = set()

    while head is not None:
        if head in visited_node:
            return True
        else:
            visited_node.add(head)
            head = head.next
    return False