# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.

# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# class Node {
#     public int val;
#     public List<Node> neighbors;
# }

# Test case format:

# For simplicity, each node's value is the same as the node's index (1-indexed). 
# For example, the first node with val == 1, the second node with val == 2, and so on. 
# The graph is represented in the test case using an adjacency list.

# An adjacency list is a collection of unordered lists used to represent a finite graph. 
# Each list describes the set of neighbors of a node in the graph.

# The given node will always be the first node with val = 1. 
# You must return the copy of the given node as a reference to the cloned graph.

from collections import deque

class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    """
    :type node: Node
    :rtype: Node
    """
    if not node:
        return None
        
    cloned_nodes = {}
    queue = deque([node])
    cloned_nodes[node] = Node(node.val)
    while queue:
        current_node = queue.popleft()
        for neighbor in current_node.neighbors:
            if neighbor not in cloned_nodes:
                cloned_nodes[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
                
            cloned_nodes[current_node].neighbors.append(cloned_nodes[neighbor])

    return cloned_nodes[node]
