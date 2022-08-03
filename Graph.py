#Graph Class Module

# Steps to use
# First create an empty class using Graph()
# Then you can add a list of nodes using add_node_list(nodes) where nodes = ["London", "Paris",....]
# You can also add a single node using add_node(node) where node = "Bombay"
# Next add edges using add_edge(node1, node2, edge). Example: x.add_edge("London", "Paris", 5). 
# This will also create a reverse edge between the given nodes.

class Graph:

    def __init__(self):
        """Initialize Class"""
        self.nodes = set() # Empty set, no duplicates
        self.graph = {} # Empty dictionary, no duplicates

    def __repr__(self):
        return str(self.graph)


    def add_node_list(self, nodes):
        """Add a list of nodes to the graph"""
        for node in nodes: 
            self.graph[node] = {} # Creates a key for each node and an empty dictionary as its value
            self.nodes.add(node) # Add each node to the node set
        return

    def add_node(self, node):
        """Add a single node to the graph"""
        self.graph[node] = {} # New key in the graph dictionary with empty dictionary as its value
        self.nodes.add(node) # Add new node to the node set
        return

    def add_edge(self, node1, node2, edge):
        """Create a weighted edge in the graph between node1 and node2"""
        # Making sure both nodes are in the graph
        if node1 not in self.nodes:
            print(node1 + " does not exist, please use add_node method.")
            return
        if node2 not in self.nodes:
            print(node2 + " does not exist, please use add_node method.")
            return
        # First we need to create a 1 way edge
        self.graph[node1][node2] = edge
        # Create a reverse edge
        self.graph[node2][node1] = edge
        return


