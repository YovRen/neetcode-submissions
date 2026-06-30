from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
            
        nodes = set()
        
        # 增加一个 parent 参数，记录是从谁走到当前 root 的
        def traverse(root, parent):
            if root in nodes:
                return False
            nodes.add(root)
            
            for neighbor in tree[root]:
                # 【核心修复】：如果邻居是我刚走过来的父亲，跳过，不当做环
                if neighbor == parent:
                    continue
                # 否则继续往下搜
                if not traverse(neighbor, root):
                    return False
            return True

        # 从节点 0 开始，0 没有父亲，随便传个 -1
        # 如果图是空的，即使返回 True，也会被下面的 len(nodes) != n 拦截
        if not edges and n > 1:
             return False
             
        if not traverse(0, -1):
            return False
            
        # 检查是否所有节点都连通
        return len(nodes) == n