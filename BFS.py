from Graphs import Graph
from queue import Queue

class BFS():

    def __init__(self, graph):
        self.graph = graph
        
    def bfs(self):
        q = Queue()
        visited = []
        parents = []
        seen = set([graph.nodes[self.start_node]])            
        q.put(graph.nodes[self.start_node])

        while not q.empty():
            node = q.get()    
            data = node.data
            neighbours = node.neighbours
            if data not in visited:
                visited.append(data)            
                for each_node in neighbours:
                    if each_node not in seen:
                        seen.add(each_node)
                        q.put(each_node)

    def shortest_path(self, start_node, end_node):
        self.start_node = start_node
        self.end_node = end_node
        self.bfs()



if __name__=="__main__":
    graph = Graph()
    q = Queue()
    graph.add_node(0, 1)
    graph.add_node(0, 3)
    graph.add_node(0, 2)
    graph.add_node(3, 1)
    graph.add_node(4, 5)
    graph.add_node(5, 8)
    graph.add_node(5, 6)
    graph.add_node(6, 7)
    graph.add_node(5, 1)
    graph.add_node(2, 6)
    graph.add_node(4, 3)    
    graph.print_graph()

    
    