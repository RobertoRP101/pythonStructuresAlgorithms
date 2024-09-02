class HashTable(object):
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size