import networkx as nx
import sys
import itertools
from CreateGraph import parse_file, create_network_graph
from GraphVerifier import check_first_node, check_diff_edge, check_same_edge

def main(file_path):
    input = parse_file(file_path)
    G = create_network_graph(input)
    if not check_first_node(G):
        return False
    
    for e1, e2 in itertools.product(G.edges):
        if not check_diff_edge(e1, e2) or not check_same_edge(e1, e2):
            return False
    
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Path name to file must be included")
    else:
        print(main(sys.argv[1]))
