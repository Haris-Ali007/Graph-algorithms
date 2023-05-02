from Graphs import Graph
from queue import Queue


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

    q = Queue()
    start_node = 0
    end_node = 5
    visited = []
    prev = []
            
    q.put(graph.nodes[start_node])
   
    while not q.empty():
        node = q.get()    
        data = node.data
        neighbours = node.neighbours
        if data not in visited:
            visited.append(data)            
            for each_node in neighbours:
                q.put(each_node)
            
