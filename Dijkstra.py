import heapq

# 1 based indexing, DAG, weighted
def Dijkstra(edges, n, src, end):
    adj = [[] for i in range(n+1)]
    for u, v, w in edges:
        adj[u].append((v, w))

    # intialize the distence list
    dist = [float('inf')] * (n+1)
    dist[src] = 0

    # initialize the priority queue (most imp component)
    pq = [(0, src)]

    while pq:
        w1, u1 = heapq.heappop(pq)

        if w1 > dist[u1]:
            continue

        for v1, w2 in adj[u1]:
            if w1 + w2 < dist[v1]:
                dist[v1] = w1 + w2
                heapq.heappush(pq, (dist[v1], v1))

    return dist[end]

# Sample Example
"""

def main():
    edges = [[1, 2, 10], [2, 3, 4], [2, 5, 1], [1, 4, 5], [4, 2, 2], [4, 5, 5]]
    ans = Dijkstra(edges, 5, 1, 5)
    print(ans) 

main()
"""