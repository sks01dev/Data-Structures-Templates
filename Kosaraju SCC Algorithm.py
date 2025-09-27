class Solution:

    def kosaraju(self, adj):
        v = len(adj)
        vis = [0] * v # visited array
        st = [] # stack to store the topo sort
        
        # Sort all edges acc to finishing time, topo sort
        def dfs1(i):
            vis[i] = 1
            
            for n in adj[i]:
                if not vis[n]:
                    dfs1(n)
            
            st.append(i)
            
        # The topo sort is now saved in the stack
        for i in range(v):
            if not vis[i]:
                dfs1(i)
            
        # Reverse the graph     
        adj2 = [[] for _ in range(v)]
        for i in range(v):
            for n in adj[i]:
                adj2[n].append(i)
                
        # DFS on the reversed graph
        def dfs2(i, temp):
            vis[i] = 1
            temp.append(i)
            
            for n in adj2[i]:
                if not vis[n]:
                    dfs2(n, temp)
                    
        # now call the dfs from the stack and it will be called for each SCC once
        c = 0
        scc = []
        vis = [0] * v
        while len(st) != 0:
            top = st.pop()
            if not vis[top]:
                temp = []
                c += 1
                dfs2(top, temp)
                scc.append(temp)
        
                
        return len(scc)
            
            
    # TC : O(V+E), SC: O(V+E)
        
        
        
