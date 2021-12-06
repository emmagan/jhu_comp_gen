import networkx as nx
import sys

## Graph Helpers
## --------------------------------------------------------------------------

def get_ordering(G):
    order = [n for n,_ in (sorted(G.nodes(data=True), key=lambda x: x[1]['order']))]
    return order

def reset_color(G):
    # set color attribute
    nx.set_edge_attributes(G,'black',name='color')
    nx.set_node_attributes(G,'tab:blue',name='color')

## --------------------------------------------------------------------------
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
            converted_edges.append((edge[0], edge[1], {'label': edge[2][:-1]}))
        E += converted_edges

    # Parse ordering, if it exists
    order = []
    first_line = fh.readline()
    name = first_line.rstrip() # Ordering
    assert(len(name) == 0 or name == "Ordering")

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
    
    reset_color(G)

    # if order exists, add it as a node attribute
    for i in range(len(order)):
        G.nodes[order[i]]['order'] = i
    
    # add stringified order as graph attribute
    G.graph['order'] = ' '.join(order)

    return G

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Path name to file must be included")
    else:
        input = parse_file(sys.argv[1])
        G = create_network_graph(input)

        print(G.nodes.data())
        print(G.edges.data())
