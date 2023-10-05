class Node:
    def __init__(self, label):
        self.label = label
        self.inbound = []  # List to store inbound links
        self.outbound = []  # List to store outbound links

class DirectedGraph:
    def __init__(self):
        self.nodes = {}  # Dictionary to store nodes in the graph

    def add_node(self, label):
        if label not in self.nodes:
            self.nodes[label] = Node(label)  # Create a new node if it doesn't exist

    def add_edge(self, from_node, to_node):
        self.add_node(from_node)  # Ensure both nodes exist in the graph
        self.add_node(to_node)
        self.nodes[from_node].outbound.append(to_node)  # Add the edge to outbound list of 'from_node'
        self.nodes[to_node].inbound.append(from_node)  # Add the edge to inbound list of 'to_node'


def identify_router(graph):
    max_connections = 0  # Initialize the maximum connections to 0
    routers_with_max_connections = []  # List to store routers with maximum connections

    # Iterate over all nodes in the graph
    for node_label in graph.nodes:
        node = graph.nodes[node_label]
        total_connections = len(node.inbound) + len(node.outbound)  # Calculate total connections for the node

        # Compare total connections to the current maximum
        if total_connections > max_connections:
            max_connections = total_connections  # Update the maximum if a higher number of connections is found
            routers_with_max_connections = [node.label]  # Initialize or replace the list with this node
        elif total_connections == max_connections:
            routers_with_max_connections.append(node.label)  # Add this node to the list if it has the same maximum

    return routers_with_max_connections  # Return the list of routers with the highest number of connections

# Test cases
graph1 = DirectedGraph()
graph1.add_edge(1, 2)
graph1.add_edge(2, 3)
graph1.add_edge(3, 5)
graph1.add_edge(5, 2)
graph1.add_edge(2, 1)
result1 = identify_router(graph1)
print(result1)  # Output: [2]

graph2 = DirectedGraph()
graph2.add_edge(1, 3)
graph2.add_edge(3, 5)
graph2.add_edge(5, 6)
graph2.add_edge(6, 4)
graph2.add_edge(4, 5)
graph2.add_edge(5, 2)
graph2.add_edge(2, 6)
result2 = identify_router(graph2)
print(result2)  # Output: [5]

graph3 = DirectedGraph()
graph3.add_edge(2, 4)
graph3.add_edge(4, 6)
graph3.add_edge(6, 2)
graph3.add_edge(2, 5)
graph3.add_edge(5, 6)
result3 = identify_router(graph3)
print(result3)  # Output: [2, 6]


# time complexity
# The time complexity of the identify_router function is primarily determined by the number of nodes in the graph since iterating over the nodes is the dominant operation. 
# Therefore, the time complexity is O(N), where N is the number of nodes in the graph.
# The function iterates over all nodes in the graph, which is a constant factor of O(N), where N is the number of nodes in the graph
# For each node, it calculates the total number of connections by summing the number of inbound and outbound links. 
# This involves simple addition and takes constant time O(1) for each node
# It compares the total connections of each node to the maximum connections found so far and updates the maximum if a higher number of connections is encountered. 
# This comparison and update operation also takes constant time O(1)
# When it finds a node with a number of connections equal to the maximum, it adds it to the list of routers with maximum connections. This operation takes constant time O(1).