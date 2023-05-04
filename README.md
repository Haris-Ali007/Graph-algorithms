# Graph Algorithms

This project is for educational purposes and provides easy implementations of basic graph implementation and traversal algorithms.

## Theory


## Usage

To use the DFS or BFS algorithm, you'll need to create an instance of the `Graph` class from the `graph.py` file. You can then call the `dfs` or `bfs` method on the graph object to traverse the graph.

Here's an example of how to create a graph and use the DFS algorithm to find a path between two nodes:

```python
from graph import Graph
from dfs import DFS

# Create a new graph
graph = Graph()

# Add nodes and edges to the graph
graph.add_node(1, 2)
graph.add_node(1, 3)
graph.add_node(2, 4)
graph.add_node(3, 5)

# Create a new DFS object and run the algorithm
dfs = DFS(graph)
visited = dfs.run_dfs(3) 

# Print the nodes in order of dfs traversal
print(visited) # Output: [5, 3]
```

You can use the same process to create and use the BFS algorithm.

## Graph implementation

The graph is implemented using adjacency list representation. Each node in the graph is represented by a dictionary, with the node value as the key and a list of its adjacent nodes as the value. Here's an example of how to create a graph using adjacency list representation:

```python
from graph import Graph

# Create a new graph
graph = Graph()

# Add nodes and edges to the graph
graph.add_node(1, 2)
graph.add_node(1, 3)
graph.add_node(2, 4)
graph.add_node(3, 5)
```

## Depth First Search

The DFS algorithm is a recursive algorithm that traverses the graph depth-first, exploring as far as possible along each branch before backtracking. In this project, the DFS algorithm is implemented in the `dfs.py` file using a stack to keep track of the nodes to be visited.

## Breadth First Search

The BFS algorithm is an iterative algorithm that traverses the graph breadth-first, visiting all the nodes at a given depth before moving on to the next level. In this project, the BFS algorithm is implemented in the `bfs.py` file using a queue to keep track of the nodes to be visited.

## Examples and Demos

To see the DFS and BFS algorithms in action, you can run the `examples.py` file. This file contains examples of how to create a graph and use the DFS and BFS algorithms to find paths between nodes.

## Contribution Guidelines

If you'd like to contribute to this project, please fork the repository and create a new branch for your changes. Once you've made your changes, create a pull request to have your changes reviewed and merged into the main branch.

## License

This project is released under the MIT License. See the `LICENSE` file for more information.
