import networkx as nx

#checks the first property of Wheeler Graph
#checks if the node with 0 in-degree comes first in the ordering
def check_first_node(graph, order):
    all_nodes = nx.nodes(graph)
    first_node = order[0]

    for node in all_nodes:
        #find the node with 0 in-degree
        if graph.in_degree(node) == 0:
            return node == first_node

#checks the second property of Wheeler Graph
#returns true if for any pair of edges e = (u, v) and e' = (u', v')
#labeled a and a' respectively, a < a' => v < b'
#returns false otherwise
def check_diff_edge(graph, order):
    all_nodes = nx.nodes(graph)
    return true
   

#checks the third property of Wheeler Graph
#returns true if for any pair of edges e = (u, v) and e' = (u', v')
#labeled a and a' respectively, (a = a') ^ (u < u') => v < v'
#returns false otherwise
def check_same_edge(graph, order):
    all_nodes = nx.nodes(graph)   
    return true
