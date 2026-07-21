# Last updated: 7/21/2026, 7:08:22 PM
from collections import defaultdict

class Node:
    def __init__(self, name):
        self.name = name
        self.children = dict()
        self.signature = ""

class Solution:
    def deleteDuplicateFolder(self, paths):
        root = Node("")
        # Build tree
        for path in paths:
            node = root
            for folder in path:
                node = node.children.setdefault(folder, Node(folder))
        
        
        signature_count = defaultdict(int)
        def dfs(node):
            if not node.children:
                node.signature = ""
                return ""
            child_sigs = []
            
            for key in sorted(node.children):
                child = node.children[key]
                child_signature = dfs(child)
                child_sigs.append("{}({})".format(key, child_signature))
            node.signature = ''.join(child_sigs)
            signature_count[node.signature] += 1
            return node.signature
        dfs(root)
        
        
        def dfs2(node, path, res):
            
            if node.signature and signature_count[node.signature] > 1:
                return
            if node.name:  
                res.append(path[:])
            for key in sorted(node.children):
                dfs2(node.children[key], path + [key], res)
        
        result = []
        for key in sorted(root.children):
            dfs2(root.children[key], [key], result)
        return result
