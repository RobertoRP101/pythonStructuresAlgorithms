class MaxHead(object):
    def __init__(self) -> None:
        self.heap = []
        
    def _left_child(self, index):
        return 2 * index + 1