from typing import List,Tuple
import collections

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.children = []

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.node_map = collections.defaultdict()
        self.count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        root = self.root
        for i in range(len(word)):
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
        c = root.count
        if root.is_end:
            c+=1
        print(prefix,c)
        return True

class Question:
    def __init__(self,topic,text):
        self.topic = topic
        self.text = text
    
    def __str__(self):
        return f"{self.text}, under topic {self.topic}"

    def __repr__(self):
        return self.__str__()

class Query(Question):
    def __str__(self):
        return "Query: " + super().__str__()

def parse_topics_into_tree(topics: str) -> TreeNode:
    pass


def read_input() -> Tuple[TreeNode,List[Question],List[Query]]:
    input_lines = []
    while True:
        try:
            input_lines.append(input())
        except EOFError:
            break
    
    topic_root = parse_topics_into_tree(input_lines[1])

    M = int(input_lines[2])
    
    questions = []

    for i in range(3,M+3):
        line = input_lines[i].split(":")

        topic = line[0].strip(" ")
        question_text = line[1].strip(" ")

        questions.append(Question(topic=topic,text=question_text))
    
    K = int(input_lines[M+3])

    queries = []
    for i in range(M+4,M+4+K):
        line = input_lines[i].split(" ")

        topic = line[0].strip(" ")
        query_text = line[1].strip(" ")

        queries.append(Query(topic=topic,text=query_text))
    
    return topic_root,questions,queries

topic_root,questions, queries = read_input()

t = Trie()
for question in questions:
    t.insert(question.text)

for q in queries:
    t.startsWith(q.text)
