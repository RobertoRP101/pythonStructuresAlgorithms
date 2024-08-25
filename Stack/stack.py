class Node(object):
    def __init__(self, value) -> None:
        self.value = value
        self.next = None   
        
        
class Stack(object):
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        