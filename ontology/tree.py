from typing import List

class TreeNode:
    def __init__(self,value):
        self.value: str = value
        self.children: List[TreeNode] = []

    def serialize(self):
        result = [self.value]
        if self.children:
            result.append("(")
            for child in self.children:
                result.append(child.serialize())
            result.append(")")

        return " ".join(result)
    

def parse_topics_into_tree_util(topic_list: List[str],processed: set) -> List[TreeNode]:
    res = []

    def has_children_topics(idx):
        if idx == len(topic_list)-1:
            return False
        for i in range(idx+1,len(topic_list)):
            if topic_list[i] != " ":
                return topic_list[i] == "("

    for i in range(len(topic_list)):
        if topic_list[i] not in processed:
            processed.add(topic_list[i])
            next_node = TreeNode(topic_list[i])
            if has_children_topics(i):
                next_node.children = parse_topics_into_tree_util(topic_list[i+2:-1],processed)
            res.append(next_node)
    return res

def parse_topics_into_tree(topics: str) -> TreeNode:
    topics = topics.strip()
    if topics == "":
        return None

    topic_list = topics.split(" ")
    if len(topic_list) == 0:
        return None
    
    root = TreeNode(topic_list[0])
    processed = set()
    processed.add("(")
    processed.add(")")
    
    for child_topic in parse_topics_into_tree_util(topic_list[2:-1],processed):
        root.children.append(child_topic)
    return root
