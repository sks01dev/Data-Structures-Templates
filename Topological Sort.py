# Topological Sort
# Given a DAG, return a valid topo ordering
def TopologicalSort(edges, n):

    adj = [[] for i in range(n+1)]
    
    # create the adjacency matrix
    for u, v in edges:
        adj[u].append(v)


    vis = [0] * (n+1) #0 -> unvisited, 1-> visiting aka in path, 2-> visited
    topo = []
    has_cycle = False

    def dfs(node):
        nonlocal has_cycle
        if has_cycle:
            return

        # mark as visting
        vis[node] = 1
        # traverse its neighbors
        for v in adj[node]:
            # if unvisited, visit it
            if vis[v] == 0:
                dfs(v)
            
            # 1 -> currently in path, has a cycle
            elif vis[v] == 1:
                has_cycle = True
                return
        
        # after traversing all the childlren, mark as visited(not in path) and add the node 
        vis[node] = 2
        topo.append(node)


    # for more than one number of SCCs (1 based indexing)
    for node in range(1, n+1):
        if not vis[node]:
            dfs(node)

    # reverse the order to make it valid topo sort (only if no cycle)
    if has_cycle:
        return []
    
    else:
        topo.reverse()
        return topo


"""
def main():
    edges = [[1,2], [2,3], [3,4], [1,5], [5,6], [6, 4]]
    n = 6

    print(TopologicalSort(edges, n))

    return 0

main()

"""