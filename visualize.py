import matplotlib.pyplot as plt
import networkx as nx
import sys



#when this is actually implemented, it will take in a graph datatype and draw it... 
#currently not sure how to only draw individual edges...have to figure that out... 


#print given graph
def visualize(G): 
    print("Hello")

    #https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx_labels.html#networkx.drawing.nx_pylab.draw_networkx_labels


    #just a sample 
    #G = nx.dodecahedral_graph()
    print(G)
    nx.draw(G)  # networkx draw()
    plt.draw()  # pyplot draw()
    plt.show()

