import argparse
import itertools
from CreateGraph import parse_file, create_network_graph
from GraphVerifier import check_first_node, check_edge_pairs, check_edge_pairs_partition
from visualize import visualize

def ordering(file_path, vis, approach):
    input = parse_file(file_path)
    G = create_network_graph(input)

    if approach == 'naive':
        is_wheeler = check_first_node(G) and check_edge_pairs(G)
    else:
        is_wheeler = check_first_node(G) and check_edge_pairs_partition(G)
    if vis:
        visualize(G,input[2])

    return is_wheeler

def no_ordering(file_path, vis, approach):
    V,E,order = parse_file(file_path)
    # ignore ordering in file
    G = create_network_graph((V,E,[]))

    for order in itertools.permutations(V):
        for i in range(len(order)):
            G.nodes[order[i]]['order'] = i

        if approach == 'naive':
            is_wheeler = check_first_node(G) and check_edge_pairs(G)
        else:
            is_wheeler = check_first_node(G) and check_edge_pairs_partition(G)

        if vis:
            visualize(G,order)
        if is_wheeler:
            break

    return is_wheeler
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', dest='path', help='Input file path name')
    parser.add_argument('-no', '--no-order', dest='order', action='store_false', help='Compute ordering (ignore file ordering)')
    parser.add_argument('-nv', '--no-vis', dest='vis', action='store_false', help='No visualization')
    parser.add_argument('-a', '--approach', dest='approach', choices=['naive', 'partition'], help='Approach (either naive or approach)')
    parser.set_defaults(order=True,vis=True,approach='naive')
    args = parser.parse_args()
    
    if args.order:
        print(ordering(args.path, args.vis, args.approach))
    else:
        print(no_ordering(args.path, args.vis, args.approach))
