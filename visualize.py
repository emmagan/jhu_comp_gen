import matplotlib
import matplotlib.pyplot as plt
import networkx as nx
from itertools import count

#when this is actually implemented, it will take in a graph datatype and draw it... 
#currently not sure how to only draw individual edges...have to figure that out... 


#print given graph
def visualize(G,order): 
    #https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx_labels.html#networkx.drawing.nx_pylab.draw_networkx_labels

    fig, ax = plt.subplots()
    ax.set_title('Order: '+ ' '.join(order))

    # get unique groups
    node_colors = nx.get_node_attributes(G,'color').values()
    edge_colors = nx.get_edge_attributes(G,'color').values()
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos = pos,with_labels=True, ax=ax, node_color=node_colors, edge_color=edge_colors)
    edge_labels = nx.get_edge_attributes(G,'label')
    formatted_edge_labels = {(elem[0],elem[1]):edge_labels[elem] for elem in edge_labels}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels,label_pos=0.5, ax=ax)
    
    plt.show()

