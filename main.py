import networkx as nx
import sys
import itertools
from CreateGraph import parse_file, create_network_graph
from GraphVerifier import check_first_node, check_edge_pairs

def main(file_path):
    input = parse_file(file_path)
    G = create_network_graph(input)
    return check_first_node(G) and check_edge_pairs(G)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Path name to file must be included")
    else:
        print(main(sys.argv[1]))
