class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #什么叫valid tree？无环？用递归思想做呢？tree=左子树valid，右子树valid
        #要不要先把树穿起来
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        #第一种就是有环，第二种就是分叉的
        nodes = set()
        def traverse(root, parent):#一直往下遍历，不会碰到两次
            if root in nodes:#碰到两次结束
                return False
            nodes.add(root)
            for node in tree[root]:#非叶子节点子树无效结束
                if node == parent:
                    continue
                if not traverse(node,root):
                    return False
            return True

        is_valid = traverse(0,-1)
        print(len(nodes))
        if len(nodes)!=n:
            return False
        else:
            return is_valid