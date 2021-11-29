class Node:
    def __init__(self, edgeVal):
        self.edge = edgeVal
        self.key = 0
        self.children = {}
    
    def getChildren(self):
        return self.children
    
    def getEdge(self):
        return self.edge 
    
    def getKey(self):
        return self.key
class Trie:
    def __init__(self):
        # sentinel node
        self.root = Node('$')
        self.totalNodes = 1
        
    def insert(self, word: str) -> None:
        if word == None or len(word) == 0:
            return

        # traverse down tree until we find a mismatch or string ends
        node = self.root
        word = word + "$" # $ is so we know where the string ends
        for w in word:
            if w not in node.children:
                newNode = Node(w)
                newNode.key = self.totalNodes
                self.totalNodes += 1
                node.children[w] = newNode
                node = newNode
            else:
                node = node.children[w]

        return

    def search(self, word: str) -> bool:
        word += '$'
        return self.startsWith(word)


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for w in prefix:
            if w not in node.children:
                return False
            else:
                node = node.children[w]

        return True
    
    def getTotalNodes(self):
        return self.totalNodes
    
    def getRoot(self):
        return self.root
    
    



