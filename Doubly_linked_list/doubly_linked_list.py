class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None   

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1