# Union Find
class UnionFind:
    def __init__(self, n: int):
        # each node is a parent of itself
        self.parent = list(range(n+1))
        self.rank = [0] * (n+1)

    # find the ultimate parent or root of a node
    def findUPar(self, node: int) -> int:
        # base case for a valid root
        if self.parent[node] == node:
            return node

        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    # check if two nodes are connected, connect them acc to rank
    def union(self, node1: int, node2: int) -> bool:
        # get the ultimate parents/ root of the 2 nodes
        par1 = self.findUPar(node1)
        par2 = self.findUPar(node2)
        # return false if they are already conected (cycle detected)
        if par1 == par2:
            return False

        if self.rank[par1] > self.rank[par2]:
            self.parent[par2] = par1

        elif self.rank[par1] < self.rank[par2]:
            self.parent[par1] = par2

        else:
            self.rank[par1] += 1
            self.parent[par2] = par1

        return True
    

# Kruskal Algorithm
def Kruskal(edges, n):
    # edges, n->vertices
    # Sort with edge weight
    edges.sort(key = lambda x: x[2])
    uf = UnionFind(n)
    mst = []

    for u, v, w in edges:
        # returns true if not in the same component, append to mst
        if uf.union(u, v):
            mst.append((u, v, w))
            # max len of any mst of graph with n vertices = n-1
            if len(mst) == n-1:
                break
    
    return mst

"""
def main():
    n = 5
    edges = [[5,4,10], [5, 2, 11], [1,2,4], [4,2,2], [4,3,2], [3,2,5], [1,5,4]]
    ans = Kruskal(edges, n)

    print(ans)

    return 0

main()

"""