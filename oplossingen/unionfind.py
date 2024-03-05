from collections import defaultdict


class UnionFind:
    def __init__(self):
        # Parent of every node
        self.parent = {}

        # Rank of every node
        # not sure if kept very clean, mainly used for union-ing efficiently
        # would advise against using it probably?
        self.rank = {}

    # Find the parent of a node
    # This performs PARTIAL path compression to speed up further
    # find operations. Could be more or less considered constant time?
    def find(self, x):
        # Create node, no parent
        if x not in self.parent:
            self.parent[x] = x
            return x

        # Existing node, own parent
        if x == self.parent.get(x, x):
            return x

        # Not own parent, continue search
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parentX = self.find(x)
        parentY = self.find(y)
        if parentX != parentY:
            px_count = self.rank.get(parentX, 1)
            py_count = self.rank.get(parentY, 1)
            combine_rank = px_count + py_count + 1
            if px_count > py_count:
                self.parent[parentY] = parentX
                self.rank[parentX] = combine_rank
            elif px_count < py_count:
                self.parent[parentX] = parentY
                self.rank[parentY] = combine_rank
            else:
                self.parent[parentY] = parentX
                self.rank[parentX] = combine_rank

    # Returns wether this node exists in the union
    def does_union_contain(self, x):
        return x in self.parent

    # Get a list of all connected nodes List[Set[]]
    def get_all_unions(self):
        children = defaultdict(list)
        for node in self.parent.keys():
            node_parent = self.find(node)
            children[node_parent].append(node)
        return children.values()

    # Return the amount of connected components
    # This _should_ equal len(self.get_all_unions())
    def calc_nbr_connected_components(self):
        return len(set(self.find(node) for node in self.parent.keys()))
