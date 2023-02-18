# Question
# A trie (pronounced as "try") or prefix tree is a tree
# data structure used to efficiently store and retrieve keys in a dataset of strings.
# There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

class Trie:

    def __init__(self):
        self.v = []

    def insert(self, word: str) -> None:
        self.v.append(word)

    def search(self, word: str) -> bool:
        return word in self.v

    def startsWith(self, prefix: str) -> bool:
        for word in self.v:
            if word.startswith(prefix):
                return True
        return False
