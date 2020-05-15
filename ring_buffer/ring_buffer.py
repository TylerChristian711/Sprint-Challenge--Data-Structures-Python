from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.current_node = None

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current_node = self.storage.head
        else:
            if not self.current_node.next:
                self.current_node.value = item
                self.current_node = self.storage.head
            else:
                self.current_node.value = item
                self.current_node = self.current_node.next

    def get(self):
        arr = []
        current = self.storage.head
        while current:
            arr.append(current.value)
            current = current.next
        return arr
