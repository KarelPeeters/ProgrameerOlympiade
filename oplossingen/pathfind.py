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
                heapq.heappush(todo, (dist + weight + heuristic(neighbor), dist + weight, neighbor, node))

    return PathfindResult(found=False, dist=None, path=None, visited=visited)
