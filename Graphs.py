
class Node:
    
    def __init__(self, data):
        self.data = data # name of the vertex
        self.neighbours = []

class Graph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, src, dest):

        if src not in self.nodes:
            self.nodes[src] = Node(src)
        if dest not in self.nodes:
            self.nodes[dest] = Node(dest)
        # store refrence of both
        self.nodes[src].neighbours.append(self.nodes[dest])
        self.nodes[dest].neighbours.append(self.nodes[src])

    def print_edges(self, node):
        if self.nodes[node] != None:
            neighbours = self.nodes[node].neighbours
            for next in neighbours:
                print(next.data)

    def print_graph(self):
        for node in self.nodes.values():
            data = node.data
            neighbours = node.neighbours
            print(f"Vertice: {data}")
            node_edges = f"{data}"
            for next in neighbours:
                node_edges = node_edges + f" --> {next.data}"
            print(f"Edges: {node_edges}")


if __name__=="__main__":
    
    g = Graph()
    g.add_node(0, 1)
    g.add_node(1, 2)
    g.add_node(2, 3)
    g.add_node(3, 4)
    g.add_node(3, 5)    
    g.print_edges(3)
    g.print_graph()
