import networkx as nx
from itertools import combinations

#checks the first property of Wheeler Graph
#checks if the node with 0 in-degree comes first in the ordering
def check_first_node(graph):
    all_nodes = nx.nodes(graph)
    order = nx.get_node_attributes(graph, 'order')
    
    for node in all_nodes:
        #find the node with 0 in-degree
        if graph.in_degree(node) == 0:
            graph.nodes[node]['color'] = 'tab:blue' if order[node] == 0 else 'red'
            return order[node] == 0
        
# NAIVE APPROACH

#checks the second and third property of Wheeler Graph
#returns true if for any pair of edges e = (u, v) and e' = (u', v')
#labeled a and a' respectively, a < a' => v < v' and (a = a') ^ (u < u') => v <= v'
#returns false otherwise
def check_edge_pairs(graph):
    all_edges = nx.edges(graph)
    order = nx.get_node_attributes(graph, 'order')
    
    for a in all_edges:
        for b in all_edges:
            #case 1: a and b are same edge, skip
            if a == b:
                continue
            a_label = graph[a[0]][a[1]]['label']
            b_label = graph[b[0]][b[1]]['label']
            #case 2: a and b are diff edges with same labels
            if a_label == b_label:
                if order[a[0]] < order[b[0]] and order[a[1]] > order[b[1]]:
                    # Color offending nodes and edges
                    nx.set_edge_attributes(graph, values={k: 'tab:red' for k in [a,b]}, name='color')
                    nx.set_node_attributes(graph, values={c: 'tab:red' for k in [a,b] for c in k}, name='color')
                    return False
            #case 3: a and b are diff edges with diff labels
            elif a_label < b_label:
                if order[a[1]] >= order[b[1]]:
                    # Color offending nodes and edges
                    nx.set_edge_attributes(graph, values={k: 'tab:red' for k in [a,b]}, name='color')
                    nx.set_node_attributes(graph, values={c: 'tab:red' for k in [a,b] for c in k}, name='color')
                    return False
    return True

# PARTITION APPROACH

#checks the second and third property of Wheeler Graph by grouping
#edges with the same labels together
def check_edge_pairs_partition(graph):
    all_edges = nx.edges(graph)
    order = nx.get_node_attributes(graph, 'order')
    edge_label_map = {}
    
    for edge in all_edges:
        label = graph[edge[0]][edge[1]]['label']
        if label not in edge_label_map:
            edge_label_map[label] = set()
        edge_label_map[label].add(edge)
    
    #check rule 3 (same label)
    for label in edge_label_map:
        edges = edge_label_map[label]
        if len(edges) > 1: #more than 1 edge with the same label
            pairs = list(combinations(edges, 2)) #generate all combinations of 2
            for edge_pair in pairs:
                a = edge_pair[0]
                b = edge_pair[1]
                if (order[a[0]] < order[b[0]] and order[a[1]] > order[b[1]]) or \
                    (order[a[0]] > order[b[0]] and order[a[1]] < order[b[1]]):
                    # Color offending nodes and edges
                    nx.set_edge_attributes(graph, values={k: 'tab:red' for k in [a,b]}, name='color')
                    nx.set_node_attributes(graph, values={c: 'tab:red' for k in [a,b] for c in k}, name='color')
                    return False

    
    #check rule 2 (diff labels)
    labels = edge_label_map.keys()
    label_pairs = list(combinations(labels, 2))
    for label_pair in label_pairs:
        #make label_1 < label_2
        if label_pair[0] < label_pair[1]:
            label_1 = label_pair[0] 
            label_2 = label_pair[1]
        else:
            label_2 = label_pair[0]
            label_1 = label_pair[1] 
        for a in edge_label_map[label_1]:
            for b in edge_label_map[label_2]:
                if order[a[1]] >= order[b[1]]:
                    # Color offending nodes and edges
                    nx.set_edge_attributes(graph, values={k: 'tab:red' for k in [a,b]}, name='color')
                    nx.set_node_attributes(graph, values={c: 'tab:red' for k in [a,b] for c in k}, name='color')
                    return False

    return True
