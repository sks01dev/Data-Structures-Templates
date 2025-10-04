def floyd_warshall(n, edges):
    INF = 10**9
    
    # Initialize distance matrix
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0  # i -> i = 0
    
    # Fill in direct edges (if undirected)
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)  
        dist[v][u] = min(dist[v][u], w)   

    # Floyd–Warshall (triple loop)
    for via in range(n):          # via (intermediate node)
        for i in range(n):      # source
            for j in range(n):  # destination
                if dist[i][via] + dist[via][j] < dist[i][j] and dist[i][via] != 1e9 and dist[via][j] != 1e9:
                    dist[i][j] = dist[i][via] + dist[via][j]

    return dist   # all-pairs shortest paths
