import networkx as nx

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
        edges = line.split(' ')
        converted_edges = []
        for e in edges:
            assert(e[0] == '(')
            assert(e[-1] == ')')
            edge = e[1:-1].split(',')
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
    G = nx.Graph()
    G.add_nodes_from(V)
    G.add_edges_from(E)

    # if order exists, add it as a node attribute
    return G

input = parse_file('data/wheeler.txt')
G = create_network_graph(input)

print(G.nodes())
print(G.edges())