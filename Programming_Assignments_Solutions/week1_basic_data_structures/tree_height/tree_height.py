# Uses Python3

'''Task. You are given a description of a rooted tree. Your task is to compute and output its height. Recall
that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.
Input Format. The first line contains the number of nodes 𝑛. The second line contains 𝑛 integer numbers
from −1 to 𝑛 − 1 — parents of nodes. If the 𝑖-th one of them (0 ≤ 𝑖 ≤ 𝑛 − 1) is −1, node 𝑖 is the root,
otherwise it’s 0-based index of the parent of 𝑖-th node. It is guaranteed that there is exactly one root.
It is guaranteed that the input represents a tree.
Constraints. 1 ≤ 𝑛 ≤ 105.
Output Format. Output the height of the tree.'''

import sys

class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

    def print(self):
        if len(self.children) == 0:
            return
        print(self.data,' --> ',end="")
        for child in self.children:
            print(child.data,end=",")
        print()
        for child in self.children:
            child.print()

    def add_children(self,nodes):
        self.children.extend([node for node in nodes])

    def max_tree_height(self):
        if len(self.children) == 0:
            max_h = 1
        else:
            max_h = 1
            for child in self.children:
                h = 1 + child.max_tree_height()
                max_h = max(h,max_h)
        return max_h

    #def max_tree_height(self):
    #    max_h = 1
    #    queue = self
    #    while(len(queue) != 0):
    #        node = queue.pop(0)
    #        queue.extend([child for child in node.children])

def create_tree(parents):
    # Create parent nodes
    nodes = []
    for i in range(len(parents)):
        nodes.append(Node(i))

    # Add children to parent nodes
    for child_id in range(len(parents)):
        if parents[child_id] == -1:
            root = nodes[child_id]
        else:
            parent_id = parents[child_id]
            nodes[parent_id].add_children([nodes[child_id]])
    return root

def main():
    n = int(input())
    a = list(map(int,input().split()[:n]))
    # Create the tree
    tree = create_tree(a)
    #tree.print()
    h = tree.max_tree_height()
    print(h)

if __name__ == '__main__':
    sys.setrecursionlimit(10**7) 
    main()
