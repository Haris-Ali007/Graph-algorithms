from Graphs import Graph


class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
    
    def dfs(self, node):
        if node in self.visited:
            return
        self.visited.append(node)
        neighbours = node.neighbours
        print(node.data, end=' ')
        for next in neighbours:
            self.dfs(next)
        
    def run_dfs(self, start_node):
        self.dfs(self.graph.nodes[start_node])        


if __name__=="__main__":
    g = Graph()
    g.add_node(0, 1)
    g.add_node(1, 2)
    g.add_node(2, 3)
    g.add_node(3, 4)
    g.add_node(3, 5)
    g.add_node(5, 6)

    d = DFS(g)
    d.run_dfs(3)