import networkx as nx

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
        
    