import heapq as hp

class MedianFind:
    def __init__(self):
        self.small = [] # max heap (store as negative values)
        self.large = [] # min heap (default in python)

    def insert(self, num):
        # check and push in respective heap
        if self.large and num > self.large[0]:
            hp.heappush(self.large, num)
        else:
            hp.heappush(self.small, -num)

        # if uneven size, rebalance by moving top element
        if len(self.small) > len(self.large) + 1:
            val = -hp.heappop(self.small)
            hp.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = hp.heappop(self.large)
            hp.heappush(self.small, -val)

    def getMedian(self):
        # if odd size, return from the heap with more elements
        if len(self.small) > len(self.large):
            return -self.small[0]
        
        if len(self.large) > len(self.small):
            return self.large[0]

        # if even size, return mean of the top two
        return (-self.small[0] + self.large[0]) / 2

mf = MedianFind()
for i in [5,3,7,11,1]:
    mf.insert(i)
    print(f"Inserted value: {i}, Median: {mf.getMedian()}")