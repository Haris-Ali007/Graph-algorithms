from Graphs import create_test_graph


class DFS:
    def __init__(self, graph):
        self.graph = graph
        self.visited = []
    
    def dfs(self, node):
        if node in self.visited:
            return
        self.visited.append(node)
        neighbours = node.neighbours
        for next in neighbours:
            self.dfs(next)
        
    def run_dfs(self, start_node):
        self.dfs(self.graph.nodes[start_node])        


if __name__=="__main__":
    test_graph = create_test_graph()
    dfs = DFS(test_graph)
    dfs.run_dfs(3)
    dfs.visited
