import Trie
import sys

trie = Trie.Trie()

# read input file and create trie
dna = open(sys.argv[1], "r")
dna_lines = dna.readlines()

for line in dna_lines:
    line = line.strip('\n')
    trie.insert(line)

trie.getOrdering()

# output wheeler graph - no ordering
graph = open(sys.argv[2], "w")
graph.write("V\n")

for i in range(trie.getTotalNodes()):
    graph.write(str(i) + " ")

graph.write("\n\nE\n")

queue = [trie.getRoot()]

while len(queue) > 0:
    node = queue.pop(0)
    count = 0
    children = node.getChildren()

    for c in children:
        if count > 0:
            graph.write(" ")
        
        graph.write("(" + str(node.vertex) + ", " + str(children[c].vertex) + ", " + str(children[c].edge) + ")")
        queue.append(children[c])
        count += 1

    if len(children) > 0:
        graph.write("\n")

graph.write("\nOrdering\n")

for i in range(trie.getTotalNodes()):
    graph.write(str(i) + " ")

graph.close()
dna.close()



    



