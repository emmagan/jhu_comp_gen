import networkx as nx
import sys
import itertools
from CreateGraph import parse_file, create_network_graph
from GraphVerifier import check_first_node, check_edge_pairs
from visualize import visualize

def main(file_path):
    input = parse_file(file_path)
    G = create_network_graph(input)

    is_wheeler = check_first_node(G) and check_edge_pairs(G)
    visualize(G,input[2])

    return is_wheeler
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Path name to file must be included")
    else:
        print(main(sys.argv[1]))
