class LinkedList:
    def __init__(self):
        self.head = None

    def find(self, key):
        curr_node = self.head

        while curr_node is not None:
            if curr_node.key == key:
                return curr_node
            curr_node = curr_node.next

        return None

    def insertAtHead(self, node):
        node.next = self.head

        self.head = node

    def delete(self, key):
        if key == self.head.key:
            self.head = self.head.next
            return self.head

        prev = None
        curr = self.head

        while curr is not None:
            if curr.key == key:
                prev.next = curr.next
                return curr

            prev = curr
            curr = curr.next
        return None