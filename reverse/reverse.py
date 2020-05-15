class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value  # val for this specific node
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            # check if current value matches what we we are looking for
            if current.get_value() == value:
                return True

            current = current.get_next()
            # value we are searching for is not in the list return false
        return False

    def printHelper(self, node, name):
        if node is None:
            print(name + " : None")
        else:
            print(name + ":" + node.value)

    def reverse_list(self, node, prev):
        # A -> B -> C -> D -> 0
        # D -> C -> B -> A  -> 0

        previous = None
        current = self.head
        while current:
            next = current.next_node
            current.next_node = previous

            previous = current
            current = next
        self.head = previous

