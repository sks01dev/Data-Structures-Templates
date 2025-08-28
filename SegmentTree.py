class SegmentTree:
    def __init__(self, total, L, R):
        self.sum = total
        self.left = None
        self.right = None
        self.L = L
        self.R = R

@staticmethod
# O(N)
def build(nums, L, R):
    if L == R:
        return SegmentTree(nums[L], L, R)

    M = (L+R) // 2
    root = SegmentTree(0, L, R)

    root.left = SegmentTree.build(nums, L, M)
    root.right = SegmentTree.build(nums, M+1, R)
    root.sum = root.left.sum + root.right.sum

    return root

# O(logn)
def update(self, index, value):
    if self.L == self.R:
        self.sum = value
        return

    M = (self.L + self.R) // 2
    if index > M:
        self.right.update(index, value)

    else:
        self.left.update(index, value)

    self.sum = self.left.sum + self.right.sum

# O(logn)
def rangeQuery(self, L, R):
    if L == self.L and R == self.R:
        return self.sum
    
    M = (self.L + self.R) // 2
    
    if L > M:
        return self.right.rangeQuery(L, R)
    elif R <= M:
        return self.left.rangeQuery(L, R)
    else:
        return (self.left.rangeQuery(L, M) + self.right.rangeQuery(M+1, R))
    