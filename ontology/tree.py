from typing import List


class TreeNode:
    def __init__(self,val):
        self.val: str = val
        self.children: List[TreeNode] = []
    def __str__(self) -> str:
        return self.val
    def __repr__(self) -> str:
        return self.val
        

def parse_topics_into_tree_util(topic_list: List[str],processed: set) -> List[TreeNode]:
    res = []

    def has_children_topics(idx):
        if idx == len(topic_list)-1:
            return True
        return topic_list[idx+1] != "("

    i = 0
    for i in range(len(topic_list)):
        if topic_list[i] not in processed:
            processed.add(topic_list[i])
            next_node = TreeNode(topic_list[i])

            if not has_children_topics(i):
                new_topic_list = topic_list[i+2:-1]
                cc = parse_topics_into_tree_util(new_topic_list,processed)
                for child_topic in cc:
                    next_node.children.append(child_topic)
            
            res.append(next_node)
    return res

def parse_topics_into_tree(topics: str) -> TreeNode:
    topic_list = topics.split(" ")
    root = TreeNode(topic_list[0])
    processed = set()
    processed.add("(")
    processed.add(")")

    for child_topic in parse_topics_into_tree_util(topic_list[2:-1],processed):
        root.children.append(child_topic)
    return root

def find_topic_node(root: TreeNode,topic: str) -> TreeNode:
    if root.val == topic:
        return root
    for child in root.children:
        if find_topic_node(child,topic) is not None:
            return child
    return None


def find_all_related_topics(root: TreeNode, topic: str) -> List[TreeNode]:
    topic_node = find_topic_node(root,topic)
    related_topics = []
    if topic_node:
        queue = [topic_node]
        while len(queue) > 0:
            current_node = queue.pop(0)
            for child in current_node.children:
                queue.append(child)
            related_topics.append(current_node)

    return related_topics
    