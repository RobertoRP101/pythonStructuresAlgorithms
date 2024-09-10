class MaxHead(object):
    def __init__(self) -> None:
        self.heap = []
        
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parents(self, index):
        return (index - 1) // 2
    