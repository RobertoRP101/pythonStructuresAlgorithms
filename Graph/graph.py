class Graph(object):
    def __init__(self):
        self.adj_list = {}
        
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])