class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 1. 终极剪枝：节点为 n 的树，边数必须是 n - 1
        if len(edges) != n - 1:
            return False
            
        # 构建邻接表
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = set()
        
        # 2. 纯粹的遍历（不需要找环，不需要管 parent）
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
                
        # 从 0 开始遍历
        dfs(0)
        
        # 3. 只要全都连起来了，配合前面的边数判断，它必定是树！
        return len(visited) == n