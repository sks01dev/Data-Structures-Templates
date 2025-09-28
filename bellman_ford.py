class Solution:
    def bellmanFord(self, V, edges, src):
        INF = int(1e8)  # commonly used in CP
        dist = [INF] * V
        dist[src] = 0

        # Relax edges V-1 times
        for _ in range(V - 1):
            updated = False
            for u, v, w in edges:
                if dist[u] != INF and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    updated = True
            # Early stop if no update
            if not updated:
                break

        # Optional: negative cycle detection
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                return [-1]

        return dist
