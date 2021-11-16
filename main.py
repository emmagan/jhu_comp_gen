import argparse
import itertools
from CreateGraph import parse_file, create_network_graph
from NaiveVerifier import check_first_node, check_edge_pairs
from visualize import visualize

def ordering(file_path):
    input = parse_file(file_path)
    G = create_network_graph(input)

    is_wheeler = check_first_node(G) and check_edge_pairs(G)
    visualize(G,input[2])

    return is_wheeler

def no_ordering(file_path):
    V,E,order = parse_file(file_path)
    # ignore ordering in file
    G = create_network_graph((V,E,[]))

    for order in itertools.permutations(V):
        for i in range(len(order)):
            G.nodes[order[i]]['order'] = i
        is_wheeler = check_first_node(G) and check_edge_pairs(G)
        visualize(G,order)
        if is_wheeler:
            break

    return is_wheeler
    
parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', dest='path', help='Input file path name')
parser.add_argument('-o', '--order', dest='order', action='store_true', help='Use ordering given in file')
parser.add_argument('-n', '--no-order', dest='order', action='store_false', help='Compute ordering (ignore file ordering)')
parser.set_defaults(order=True)
args = parser.parse_args()

if args.order:
    print(ordering(args.path))
else:
    print(no_ordering(args.path))
