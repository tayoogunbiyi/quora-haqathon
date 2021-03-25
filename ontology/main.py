from typing import List,Tuple

from trie import Trie
from tree import TreeNode, find_all_related_topics,parse_topics_into_tree

class Question:
    def __init__(self,topic,text):
        self.topic = topic.strip()
        self.text = text.strip()
    
    def __str__(self):
        return f"{self.text}, under topic {self.topic}"

    def __repr__(self):
        return self.__str__()

class Query(Question):
    def __str__(self):
        return "Query: " + super().__str__()

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
        idx = input_lines[i].index(" ")
        topic = input_lines[i][0:idx]
        query_text = input_lines[i][idx+1:].strip()
        queries.append(Query(topic=topic,text=query_text))
    
    return topic_root,questions,queries

topic_root,questions, queries = read_input()

t = Trie()
for question in questions:
    t.insert(question.text,question.topic)
    
for q in queries:
    topic_map, count = t.countQuestionsWithPrefixAndTopic(q.text,q.topic)
    related_topics = set([v.val for v in find_all_related_topics(topic_root,q.topic)])
    ans = 0
    for k in topic_map:
        if k in related_topics:
            ans += topic_map[k]
    
    print(ans)

