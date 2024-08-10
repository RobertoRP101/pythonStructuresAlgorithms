class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None        

class LinkedList(object):
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node
        self.length = 1 