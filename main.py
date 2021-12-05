import argparse
import itertools
import logging
import math
from tqdm import tqdm
from CreateGraph import parse_file, create_network_graph, get_ordering, reset_color
from GraphVerifier import check_first_node, check_edge_pairs, check_edge_pairs_partition
from visualize import vis_multiple, vis_single

def ordering(file_path, vis, approach):
    logging.info('Parsing input file')
    input = parse_file(file_path)

    logging.info('Creating networkx graph')
    G = create_network_graph(input)

    logging.info('Checking ordering')
    if approach == 'naive':
        is_wheeler = check_first_node(G) and check_edge_pairs(G)
    else:
        is_wheeler = check_first_node(G) and check_edge_pairs_partition(G)
    
    logging.info('Creating visualization')
    if vis:
        vis_single(G)

    return is_wheeler

def no_ordering(file_path, vis, approach):
    logging.info('Parsing input file')
    V,E,order = parse_file(file_path)

    logging.info('Creating networkx graph')
    # ignore ordering in file
    G = create_network_graph((V,E,[]))

    if vis:
        logging.info('Creating visualization')
        # press q to quit visualization
        v = vis_multiple(G, generator, approach)

        # if we broke out of the generator, we just have to check the last iteration to see if the final graph is wheeler
        if approach == 'naive':
            is_wheeler = check_first_node(G) and check_edge_pairs(G)
        else:
            is_wheeler = check_first_node(G) and check_edge_pairs_partition(G)
    else:
        logging.info('Checking ordering')
        is_wheeler = any(generator(G,approach))
    
    return get_ordering(G) if is_wheeler else is_wheeler

# Encapsulate all side effects into this generator.
# This iterates through all permutations of orderings and
# updates the color and order labels in the graph.
# We can't use a regular function here because of how we are
# animating multiple graphs.
def generator(G,approach):
    for order in tqdm(itertools.permutations(G.nodes), total=math.factorial(len(G.nodes))):
        reset_color(G)

        for i in range(len(order)):
            G.nodes[order[i]]['order'] = i

        G.graph['order'] = ' '.join(order)

        if approach == 'naive':
            is_wheeler = check_first_node(G) and check_edge_pairs(G)
        else:
            is_wheeler = check_first_node(G) and check_edge_pairs_partition(G)

        yield is_wheeler
        if is_wheeler:
            break
    
if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)
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
