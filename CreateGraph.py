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
            break  # end of file
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
            break  # end of file
        edges = line.split(' ')
        E += edges

    # Parse ordering, if it exists
    order = []
    first_line = fh.readline()
    name = first_line.rstrip() # Ordering
    assert(name == "Ordering")

    while True:
        line = fh.readline().rstrip()
        if len(line) == 0:
            break  # end of file
        o = line.split(' ')
        order += o

    # Ignore source link and close file handle
    fh.close()

    return (V, E, order)

V, E, order = parse_file('data/wheeler.txt')
print(V)
print(E)
print(order)