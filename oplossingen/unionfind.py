class UnionFind:
    def __init__(self, size):
        # Input amount of nodes
        self.size = size

        # Parent of every node
        self.parent = [i for i in range(size)]

        # Rank of every node
        # not sure if kept very clean, mainly used for union-ing efficiently
        # would advise against using it probably?
        self.rank = [1] * size

    # Find the parent of a node
    # This performs PARTIAL path compression to speed up further
    # find operations. Could be more or less considered constant time?
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            if self.rank[parentX] > self.rank[parentY]:
                self.parent[parentY] = parentX
            elif self.rank[parentX] < self.rank[parentY]:
                self.parent[parentX] = parentY
            else:
                self.parent[parentY] = parentX
                self.rank[parentX] += 1

    def calc_nbr_connected_components(self):
        return len(set(self.find(i) for i in range(self.size)))
