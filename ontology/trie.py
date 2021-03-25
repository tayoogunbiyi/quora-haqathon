import collections

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = collections.defaultdict()
        self.number_of_descendant_words = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        word = word.lower()

        root = self.root
        for ch in word:
            ch = ch.lower()
            root.number_of_descendant_words += 1
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        root.is_word = True
        
    def contains(self, word: str) -> bool:
        root = self.root
        for ch in word:
            ch = ch.lower()
            if ch not in root.children:
                return False
            root = root.children[ch]
        return root.is_word
    
    def count_words_starting_with(self,prefix: str) -> int:
        root = self.root
        for ch in prefix:
            ch = ch.lower()
            if ch not in root.children:
                return 0
            root = root.children[ch]
        
        result = root.number_of_descendant_words
        if root.is_word:
            result += 1
        return result
