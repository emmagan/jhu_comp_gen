from matplotlib import pyplot as plt, animation
from functools import partial
import networkx as nx

# single ordering
def vis_single(G):
    fig, ax = plt.subplots()
    pos = nx.spring_layout(G)
    update(0,G,pos,ax)
    plt.show()

# multiple orderings -> animation
def vis_multiple(G, generator, approach):
    fig, ax = plt.subplots()
    pos = nx.spring_layout(G)
    ani = animation.FuncAnimation(fig, update, frames=partial(generator,G,approach), fargs=(G, pos, ax), repeat=False)
    plt.show()
    return ani

#https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx_labels.html#networkx.drawing.nx_pylab.draw_networkx_labels
def update(i,G,pos,ax): 
    # set axis title
    ax.set_title('Order: '+G.graph['order'])

    # get unique groups
    node_colors = nx.get_node_attributes(G,'color').values()
    edge_colors = nx.get_edge_attributes(G,'color').values()

    # draw nodes
    nx.draw(G, pos = pos,with_labels=True, ax=ax, node_color=node_colors, edge_color=edge_colors)

    # draw edges
    edge_labels = nx.get_edge_attributes(G,'label')
    formatted_edge_labels = {(elem[0],elem[1]):edge_labels[elem] for elem in edge_labels}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=formatted_edge_labels,label_pos=0.5, ax=ax)
