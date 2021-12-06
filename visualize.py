from matplotlib import pyplot as plt, animation
from functools import partial
import networkx as nx

# single ordering
def vis_single(G, fname):
    fig, ax = plt.subplots()
    pos = nx.spring_layout(G)
    update(0,G,pos,ax)
    plt.show()
    if len(fname) != 0:
        plt.savefig(fname)

# multiple orderings -> animation
def vis_multiple(G, generator, approach, f):
    fig, ax = plt.subplots()
    pos = nx.spring_layout(G)
    # saving as a gif defaults to 100 frames, so update save_count if you want more frames included
    ani = animation.FuncAnimation(fig, update, frames=partial(generator,G,approach), fargs=(G, pos, ax), repeat=False, save_count=473)

    # This saves the animation as a gif
    if len(f) != 0:
        writergif = animation.PillowWriter(fps=30) 
        ani.save(f, writer=writergif)

    plt.show()
    return ani

#https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx_labels.html#networkx.drawing.nx_pylab.draw_networkx_labels
def update(i,G,pos,ax):
    # clear old axis and set axis title
    ax.clear()
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
