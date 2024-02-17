from typing import List, TypeVar, Dict, Tuple, Set


def readline(f=None) -> str:
    if f is None:
        return input().strip()
    else:
        return f.readline().strip()


def readints(f=None) -> List[int]:
    line = readline(f)
    if not line:
        return []
    return [int(x) for x in line.split(" ")]


def ortho_neighbors(h, w, y, x):
    mid = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    return [(ny, nx) for ny, nx in mid if 0 <= ny < h and 0 <= nx < w]


T = TypeVar("T")


def dijkstra(graph: Dict[T, Tuple[T, float]], starts: Set[T], ends: Set[T]):
    # def dijkstra(graph, starts, ends):
    """
    graph: dict of node -> (neighbor, distance)
    starts: set of start nodes, all assumed with cost 0
    ends: set of end nodes

    returns: (distance, path including start and end)
    """

    import heapq

    # priority queue of (dist, node, parent)
    todo = [(0, start, None) for start in starts]
    heapq.heapify(todo)

    # node -> best parent
    visited = {}

    while todo:
        dist, node, parent = heapq.heappop(todo)
        # print(f"popped {dist, node, parent}")
        if node in visited:
            continue
        visited[node] = parent

        if node in ends:
            # print(f"end node {node}")
            path = []
            curr = node
            while curr is not None:
                path.append(curr)
                curr = visited[curr]
            path.reverse()
            return dist, path

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(todo, (dist + weight, neighbor, node))

    # TODO return all distances instead?
    return None
