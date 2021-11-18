class Node:
    def __init__(self, value):
        self.val = value
        self.children = {}
class Trie:
    def __init__(self):
        # sentinel node
        self.root = Node('$')

    def insert(self, word: str) -> None:
        if word == None or len(word) == 0:
            return

        # traverse down tree until we find a mismatch or string ends
        node = self.root
        word = word + "$" # $ is so we know where the string ends
        for w in word:
            if w not in node.children:
                newNode = Node(w)
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
