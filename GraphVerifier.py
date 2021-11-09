import networkx as nx

#checks if the node with 0 in-degree comes first in the ordering
def check_first_node(graph, order):
    all_nodes = nx.nodes(graph)
    first_node = order[0]

    for node in all_nodes:
        #find the node with 0 in-degree
        if graph.in_degree(node) == 0:
            return node == first_node
