import heapq

def prims(n, graph):
    visited = [False] * n
    min_heap = [(0, 0)]   # (weight, node), start from node 0
    total_cost = 0

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:
            continue
        # visit now 
        visited[u] = True
        total_cost += weight

        # push unvisited adjacent nodes into the min heap 
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return total_cost # mst cost
