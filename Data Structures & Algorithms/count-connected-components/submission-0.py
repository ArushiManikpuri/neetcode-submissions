class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #Step:1 build an adjacency list:
        adj = {i:[] for i in range(n)}
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        result = 0
        #Step2 :#dfs traversal
        def dfs(node):
            if node in visit:
                return 
            visit.add(node)
            for nei in adj[node]:
                dfs(nei)
        #Step 3: Count the components    
        for i in range(n):
            if i not in visit:
                dfs(i)
                result += 1
        
        return result           

        