from typing import List

from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, List, Dict, Tuple, Callable, Iterable

T = TypeVar("T")


@dataclass
class PathfindResult(Generic[T]):
    found: bool
    dist: Optional[float]
    path: Optional[List[T]]

    visited: Dict[T, Tuple[float, Optional[T]]]


def pathfind(starts: List[T], next: Callable[[T], Tuple[bool, Iterable[Tuple[T, float]]]],
             heuristic: Callable[[T], float] = lambda _: 0) -> PathfindResult[T]:
    """
    An implementation of A*.

    starts: list of start nodes, all assumed with cost 0
    next: callable (node) -> (is_end, [(neighbor, dist)])
    heuristic: callable (node) -> float

    note: this can also be used to:
    * compute the distance too all nodes in the graph, just always return is_end=False and read result.visited
    * floodfill, same as before but ignore all distances
    """

    import heapq

    # priority queue of (dist+heuristic, dist, node, parent)
    todo: List[(float, float, T, Optional[T])] = [(0 + heuristic(s), 0, s, None) for s in starts]
    heapq.heapify(todo)

    # node -> (best_dist, best_parent)
    visited = {}

    while todo:
        _, dist, node, parent = heapq.heappop(todo)

        if node in visited and visited[node][0] <= dist:
            continue
        visited[node] = (dist, parent)

        # print(f"Visiting {node} with dist {dist}")

        is_end, neighbors = next(node)

        if is_end:
            path = []
            curr = node
            while curr is not None:
                path.append(curr)
                _, curr = visited[curr]
            path.reverse()
            return PathfindResult(found=True, dist=dist, path=path, visited=visited)

        for neighbor, weight in neighbors:
            if neighbor not in visited:
                # print(f"neigh {neighbor}")
                heapq.heappush(todo, (dist + weight + heuristic(neighbor), dist + weight, neighbor, node))

    return PathfindResult(found=False, dist=None, path=None, visited=visited)



def readline(f=None) -> str:
    if f is None:
        return input().strip()
    else:
        return f.readline().strip()


def readint(f=None) -> int:
    return int(readline(f))


def readints(f=None) -> List[int]:
    line = readline(f)
    if not line:
        return []
    return [int(x) for x in line.split(" ")]


def ortho_neighbors(h, w, y, x):
    mid = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
    return [(ny, nx) for ny, nx in mid if 0 <= ny < h and 0 <= nx < w]


cases = readint()

for case in range(cases):
    a, b, p, n, k = readints()
    # print(a, b, p, n, k)

    graph = {}
    for _ in range(k):
        s, e, d = readints()

        # print(s, e, d)
        graph.setdefault(s, {})[e] = d
        # graph.setdefault(e, {})[s] = d

    # print(graph)
    r = pathfind([a], lambda curr: (curr == b, graph.get(curr, {}).items()))
    assert r.found

    # print("graph", graph)

#     print("path", r.path)
#     print("dist", r.dist)

    times = {}
    prev = None
    curr_time = -2
    for curr in r.path:
        if prev is not None:
            curr_time += graph[prev][curr]
        times[curr] = curr_time
        prev = curr

#     print("times", times)

    p_result = pathfind([p], lambda curr: (False, graph.get(curr, {}).items()))
    assert not p_result.found

#     print(p_result)

    best_key = None
    best_result = None

    for curr, time in times.items():
        if curr in p_result.visited:
            pdist = p_result.visited[curr][0]
            tdist = time
            key = (pdist, tdist)

            if pdist > tdist:
                continue

            if best_key is None or key < best_key:
                best_key = key
                best_result = (curr, pdist)

#     print("result")
    if best_result is None:
        print(case+1, "ONMOGELIJK")
    else:
        print(case + 1, *best_result)

    # print(result)
    # print(" ".join(str(x) for x in result))
