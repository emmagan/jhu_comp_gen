import argparse
import itertools
import logging
import math
from tqdm import tqdm
from CreateGraph import parse_file, create_network_graph, get_ordering, reset_color
from GraphVerifier import check_first_node, check_edge_pairs, check_edge_pairs_partition
from visualize import vis_multiple, vis_single

def ordering(input, vis, approach, save):
    logging.info('Creating networkx graph')
    G = create_network_graph(input)

    logging.info('Checking ordering')
    if approach == 'naive':
        is_wheeler = check_first_node(G) and check_edge_pairs(G)
    else:
        is_wheeler = check_first_node(G) and check_edge_pairs_partition(G)
    
    if vis:
        logging.info('Creating visualization')
        vis_single(G, save)

    return is_wheeler

def no_ordering(input, vis, approach, save):
    logging.info('Creating networkx graph')
    # ignore ordering in file
    G = create_network_graph(input)

    if vis:
        logging.info('Creating animation visualization')
        # press q to quit visualization
        v = vis_multiple(G, generator, approach, save)

        # if we broke out of the generator, we just have to check the last iteration to see if the final graph is wheeler
        if approach == 'naive':
            is_wheeler = check_first_node(G) and check_edge_pairs(G)
        else:
            is_wheeler = check_first_node(G) and check_edge_pairs_partition(G)
    else:
        logging.info('Checking orderings')
        is_wheeler = any(generator(G,approach))
    
    return get_ordering(G) if is_wheeler else is_wheeler

# Encapsulate all side effects into this generator.
# This iterates through all permutations of orderings and
# updates the color and order labels in the graph.
# We can't use a regular function here because of how we are
# animating multiple graphs.
def generator(G,approach):
    if len(G.nodes) < 170: # 170 is the min before we get an overflow error
        iterator = tqdm(itertools.permutations(G.nodes), total=math.factorial(len(G.nodes)))
    else:
        logging.warning('Simplified progress bar shown due to large total number of iterations')
        iterator = tqdm(itertools.permutations(G.nodes))

    for order in iterator:
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
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', dest='path', help='Input file path name', required=True)
    parser.add_argument('-a', '--approach', dest='approach', choices=['naive', 'partition'], help='Approach (either naive or approach)', required=True)
    parser.add_argument('-s', '--output-path', dest='save', help='Output file path name for png or gif file (visualization must be on)', default="")
    parser.add_argument('-no', '--no-order', dest='order', default=True, action='store_false', help='Compute ordering (ignore file ordering)')
    parser.add_argument('-nv', '--no-vis', dest='vis', default=True, action='store_false', help='No visualization')
    parser.add_argument('-l', '--log', dest='log', default=1, help='Logging level 0=none 1=info (defaults to info level)')
    args = parser.parse_args()
    
    level = logging.INFO if args.log==1 else logging.WARNING
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=level)

    logging.info('Parsing input file')
    input = parse_file(args.path)

    if args.order and len(input[2]) != 0:
        print(ordering(input, args.vis, args.approach, args.save))
    else:
        print(no_ordering(input, args.vis, args.approach, args.save))
