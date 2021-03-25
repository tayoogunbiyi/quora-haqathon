import collections

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.node_map = collections.defaultdict()
        self.count = 0
        self.topic_map = collections.Counter()
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str,topic: str) -> None:
        root = self.root
        for i in range(len(word)):
            root.topic_map[topic]+=1
            root.count += 1
            if word[i] not in root.node_map:
                root.node_map[word[i]] = TrieNode()
            root = root.node_map[word[i]]
        root.is_end = True
        

    def search(self, word: str) -> bool:
        root = self.root
        for ch in word:
            if ch not in root.node_map:
                return False
            root = root.node_map[ch]
        
        return root.is_end
        

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for ch in prefix:
            if ch not in root.node_map:
                return False
            root = root.node_map[ch]
        # c = root.count
        # if root.is_end:
        #     c+=1
        # print(prefix,c)
        return True
    
    def countQuestionsWithPrefixAndTopic(self,prefix: str, topic: str) -> int:
        root = self.root
        for ch in prefix:
            if ch not in root.node_map:
                return {},0
            root = root.node_map[ch]
        # print(f"prefix = {prefix}, root.count = {root.count}, root.topic_map = {root.topic_map}")
        # print(root.topic_map)
        result = root.count
        if root.is_end:
            result += 1
        return root.topic_map,result
       

