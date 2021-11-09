import networkx as nx
import sys

def parse_file(file):
    """ Parse wheeler graph (V,E,ordering) from a file path name. """
    # Open file handle
    fh = open(file,'r')

    # Parse vertices
    V = []
    first_line = fh.readline()
    name = first_line.rstrip() # V
    assert(name == "V")

    while True:
        line = fh.readline().rstrip()
        if len(line) == 0:
            break  # end of vertex section
        vertices = line.split(' ')
        V += vertices

    # Parse edges
    E = []
    first_line = fh.readline()
    name = first_line.rstrip() # E
    assert(name == "E")

    while True:
        line = fh.readline().rstrip()
        if len(line) == 0:
            break  # end of edges section
        edges = [l.strip() for l in line.split('(') if l]
        converted_edges = []
        for e in edges:
            assert(e[-1] == ')')
            edge = [ed.strip() for ed in e.split(',')]
            converted_edges.append((edge[0], edge[1], {'label': edge[2]}))
        E += converted_edges

    # Parse ordering, if it exists
    order = []
    first_line = fh.readline()
    name = first_line.rstrip() # Ordering
    assert(name == "Ordering")

    while True:
        line = fh.readline().rstrip()
        if len(line) == 0:
            break  # end of ordering section
        o = line.split(' ')
        order += o

    # Ignore source link and close file handle
    fh.close()

    return (V, E, order)

def create_network_graph(graph):
    V,E,order = graph
    G = nx.DiGraph()
    G.add_nodes_from(V)
    G.add_edges_from(E)

    # if order exists, add it as a node attribute
    for i in range(len(order)):
        G.nodes[order[i]]['order'] = i
    return (G, order)

#checks if the node with 0 in-degree comes first in the ordering
def check_first_node(graph, order):
    all_nodes = nx.nodes(graph)
    first_node = order[0]

    for node in all_nodes:
        #find the node with 0 in-degree
        if graph.in_degree(node) == 0:
            return node == first_node
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Path name to file must be included")
    else:
        input = parse_file(sys.argv[1])
        G,order = create_network_graph(input)
        first_node_valid = check_first_node(G, order)	

        print(G.nodes.data())
        print(G.edges.data())
        print(first_node_valid)
