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
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node    
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next