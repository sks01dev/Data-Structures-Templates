import heapq

def prims_mst(n: int, graph: List[List[Tuple[int,int]]]) -> int:
    """
    Computes the Minimum Spanning Tree (MST) cost using Prim's algorithm.

    Parameters:
        n     : number of nodes (0-indexed 0..n-1)
        graph : adjacency list, graph[u] = [(v, weight), ...]

    Returns:
        Total weight of MST if the graph is connected, else -1.

    Time Complexity:
        O(E log V) where E = number of edges, V = number of nodes
        Explanation: Each edge may be pushed to the heap at most once, and
                     each heap operation costs O(log V).

    Space Complexity:
        O(V + E) for adjacency list + min-heap + visited array
    """
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, node), start from node 0
    total_cost = 0

    while min_heap:
        w, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True          # include node u in MST
        total_cost += w            # add edge weight to total
        for v, wt in graph[u]:     # push all edges from u to unvisited nodes
            if not visited[v]:
                heapq.heappush(min_heap, (wt, v))

    # check if all nodes are included (graph might be disconnected)
    return total_cost if all(visited) else -1


# ---------------- Example ----------------
if __name__ == "__main__":
    edges = [
        (0, 1, 2), (0, 3, 6), (1, 2, 3),
        (1, 3, 8), (1, 4, 5), (2, 4, 7), (3, 4, 9)
    ]
    n = 5

    # build adjacency list
    graph: List[List[Tuple[int,int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # undirected graph

    print(prims_mst(n, graph))  # Output: 16
